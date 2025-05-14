To-Do List Application

Overview

The To-Do List is a web-based application that allows users to create and manage their tasks securely. Users can sign up for an account, log in, and perform task management operations such as creating, viewing, and deleting tasks. The application is built with a modern technology stack, containerized using Docker, and orchestrated with Docker Compose, ensuring scalability and ease of deployment.

Features





User Registration (Sign Up): Create a new account with a unique username and password.



User Authentication (Login): Log in to access personalized task management.



Task Management:





Create tasks with a title and description.



View a list of all tasks associated with the logged-in user.



Delete tasks.

Technology Stack





Backend: FastAPI (Python) - A high-performance web framework for building APIs.



Database: MySQL - A relational database for storing user and task data.



Frontend: HTML, CSS, JavaScript - A simple, responsive user interface.



Containerization: Docker - For packaging the backend service.



Orchestration: Docker Compose - For managing multi-container services (backend and database).



Authentication: JWT (JSON Web Tokens) - For secure user authentication.

Prerequisites

To run this application, ensure you have the following installed:





Docker and Docker Compose



Git



A web browser (e.g., Chrome, Firefox)

Setup Instructions

Follow these steps to set up and run the application locally:





Clone the Repository:

git clone https://github.com/Muhamed-Abdelrahman/todo-list-docker.git
cd todo-list



Build and Run with Docker Compose:

docker compose up --build

This command builds the backend Docker image and starts both the backend and MySQL services.



Access the Application:





Open your browser and navigate to: http://localhost:8000/static/signup.html



Sign Up: Create a new account with a username and password.



Login: Use your credentials to log in.



Manage Tasks: After logging in, you will be redirected to the task management page where you can create, view, and delete tasks.



Stop the Application:





Press Ctrl+C in the terminal to stop the containers.



To remove containers and networks:

docker compose down

DockerHub Repository

The Docker image for the backend is published to DockerHub: https://hub.docker.com/r/your-username/todo-list

To pull and use the image:

docker pull your-username/todo-list:latest

Running Locally Without Docker

If you prefer to run the application without Docker:





Install Dependencies:





Python 3.9+



MySQL Server



Install Python packages:

pip install -r requirements.txt



Configure MySQL:





Create a database named todo_db.



Update main.py with your MySQL credentials if different from the defaults (todo_user, todo_password).



Run the Application:

uvicorn main:app --host 0.0.0.0 --port 8000



Access the application at http://localhost:8000/static/signup.html.

Project Structure

todo-list/
├── frontend/
│   ├── index.html         # Task management page
│   ├── signup.html        # Sign-up page
│   ├── login.html         # Login page
│   ├── styles.css         # CSS styles
│   └── script.js          # Frontend JavaScript logic
├── Dockerfile            # Docker configuration for backend
├── docker-compose.yml    # Orchestration for backend and MySQL
├── main.py               # FastAPI backend code
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── ProjectSummary.md     # Project summary

Troubleshooting





MySQL Connection Issues: If the backend fails to connect to MySQL, ensure the MySQL service is fully started. Wait a few seconds and retry docker compose up.



Port Conflicts: If port 8000 or 3306 is in use, stop other services or change the ports in docker-compose.yml.



JWT Errors: Ensure the SECRET_KEY in main.py is consistent across deployments.

Team





[Your Name] - Sole Developer

License

This project is licensed under the MIT License.
