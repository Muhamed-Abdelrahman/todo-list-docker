from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
import mysql.connector
import os
import jwt
from datetime import datetime, timedelta

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# MySQL connection
def get_db():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        user=os.getenv("MYSQL_USER", "todo_user"),
        password=os.getenv("MYSQL_PASSWORD", "todo_password"),
        database=os.getenv("MYSQL_DATABASE", "todo_db")
    )
    return conn

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = "your-secret-key"  # Change this in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Pydantic models
class User(BaseModel):
    username: str
    password: str

class Task(BaseModel):
    title: str
    description: str

# Create database tables
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_db()

# JWT functions
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return username

# Routes
@app.post("/signup")
async def signup(user: User):
    conn = get_db()
    cursor = conn.cursor()
    try:
        password_hash = pwd_context.hash(user.password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (user.username, password_hash))
        conn.commit()
        return {"message": "User created successfully"}
    except mysql.connector.IntegrityError:
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        cursor.close()
        conn.close()

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (form_data.username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not user or not pwd_context.verify(form_data.password, user["password_hash"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/tasks")
async def create_task(task: Task, current_user: str = Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id FROM users WHERE username = %s", (current_user,))
    user = cursor.fetchone()
    cursor.execute("INSERT INTO tasks (user_id, title, description) VALUES (%s, %s, %s)", 
                   (user["id"], task.title, task.description))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task created successfully"}

@app.get("/tasks")
async def get_tasks(current_user: str = Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id FROM users WHERE username = %s", (current_user,))
    user = cursor.fetchone()
    cursor.execute("SELECT id, title, description FROM tasks WHERE user_id = %s", (user["id"],))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id FROM users WHERE username = %s", (current_user,))
    user = cursor.fetchone()
    cursor.execute("DELETE FROM tasks WHERE id = %s AND user_id = %s", (task_id, user["id"]))
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task deleted successfully"}
