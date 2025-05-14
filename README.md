To-Do List Application

Overview

The To-Do List application is a secure, intuitive, and scalable web platform designed to simplify personal task management. It empowers users to create accounts, authenticate securely, and organize their tasks by creating, viewing, and deleting them through a clean and responsive interface. Built with a modern technology stack, the application leverages FastAPI for high-performance APIs, MySQL for reliable data storage, and a lightweight frontend for seamless user interaction. Containerized with Docker and orchestrated using Docker Compose, the application ensures consistent deployment across environments, making it an ideal solution for both personal use and educational purposes. This project showcases best practices in full-stack development, secure authentication, and DevOps workflows, reflecting a production-ready approach to software engineering.

Features

The To-Do List application offers a robust set of features to enhance productivity and user experience:





User Registration (Sign Up): Users can create a new account by providing a unique username and password. Passwords are hashed using bcrypt for maximum security and stored in a MySQL database. The registration process includes validation to prevent duplicate usernames and provides clear feedback for invalid inputs.



User Authentication (Login): Secure login is implemented using JSON Web Tokens (JWT). Users authenticate with their credentials, receiving a JWT token stored client-side to access protected routes. The system ensures only authenticated users can manage their tasks, with robust error handling for invalid credentials.



Task Management:





Create Tasks: Authenticated users can add tasks with a required title and an optional description. Tasks are stored in the MySQL database, linked to the user's ID for personalized access.



View Tasks: Displays a dynamic, paginated list of tasks specific to the logged-in user, retrieved efficiently from the backend and rendered on the frontend.



Delete Tasks: Users can remove tasks with a single click, with immediate updates reflected in the database and user interface, ensuring a responsive experience.



Responsive Interface: The frontend, built with HTML, CSS, and JavaScript, adapts to various devices, providing a consistent experience on desktops, tablets, and smartphones. The design prioritizes simplicity and usability.



Error Handling and Feedback: The application handles edge cases (e.g., network issues, invalid inputs, or database errors) gracefully, delivering meaningful error messages to guide users.

Technology Stack

The application is built using a carefully selected, industry-standard technology stack to ensure performance, scalability, and maintainability:





Backend:





FastAPI (Python): A high-performance, asynchronous framework for building RESTful APIs. FastAPI is chosen for its speed, automatic OpenAPI documentation, and ease of handling asynchronous requests.



Uvicorn: An ASGI server that runs the FastAPI application, supporting concurrent connections for efficient request processing.



Database:





MySQL 8.0: A relational database for storing user credentials (username, hashed password) and tasks (title, description, user ID). MySQL is selected for its reliability, support for structured data, and robust querying capabilities.



Frontend:





HTML, CSS, JavaScript: A lightweight, responsive frontend stack that delivers a dynamic user interface. JavaScript handles client-side logic, including AJAX requests to the backend and real-time UI updates.



Static File Serving: FastAPI serves frontend files from the frontend/ directory under the /static endpoint, ensuring fast access to assets.



Containerization:





Docker: Packages the backend application, dependencies, and frontend files into a portable container based on the python:3.9-slim image. Docker ensures consistency across development and production environments.



Dockerfile: Defines the build process, including dependency installation, file copying, and security configurations (e.g., running as a non-root user).



Orchestration:





Docker Compose: Manages the application's services (FastAPI backend and MySQL database) within a custom bridge network (app-network). It configures environment variables, port mappings, and health checks for reliable service startup and communication.



Authentication:





JWT (PyJWT): Provides stateless, secure authentication by generating and validating JSON Web Tokens for protected API endpoints.



bcrypt (passlib): Hashes passwords securely, protecting user credentials against unauthorized access.



Additional Libraries:





python-multipart: Enables parsing of form data for login requests using OAuth2PasswordRequestForm.



aiofiles: Supports asynchronous file operations for efficient static file serving.



mysql-connector-python: Facilitates secure communication between the FastAPI backend and MySQL database.

Prerequisites

To run the To-Do List application, ensure the following tools are installed:





Docker: Version 20.10 or higher, for building and running containers.



Docker Compose: Version 1.29 or higher, for orchestrating multi-container services.



Git: For cloning the repository.



Web Browser: A modern browser (e.g., Chrome, Firefox, or Edge) for accessing the application.



Optional (for non-Docker setup):





Python 3.9 or higher.



MySQL Server 8.0 or higher.



pip for installing Python dependencies.

Setup Instructions

Follow these steps to set up and run the application locally:





Clone the Repository:

git clone https://github.com/Muhamed-Abdelrahman/todo-list-docker.git
cd todo-list-docker



Build and Run with Docker Compose:

docker compose up --build





This command builds the backend Docker image (dracola1/todo-list:latest) and starts the FastAPI backend and MySQL services.



The backend runs on http://localhost:8000, and MySQL is mapped to port 3307 (to avoid conflicts with local MySQL instances on port 3306).



Access the Application:





Open your browser and navigate to:

http://localhost:8000/static/signup.html



Sign Up: Create a new account with a unique username and password.



Login: Use your credentials to log in and access the task management page.



Manage Tasks: Create, view, and delete tasks as needed.



Stop the Application:





Press Ctrl+C in the terminal to stop the containers.



To remove containers, networks, and volumes:

docker compose down

DockerHub Repository

The Docker image for the To-Do List application is published on DockerHub:

https://hub.docker.com/r/dracola1/todo-list

To pull and use the image:

docker pull dracola1/todo-list:latest

Then, run the application using the provided docker-compose.yml:

docker compose up

Running Locally Without Docker

If you prefer to run the application without Docker, follow these steps:





Install Dependencies:





Ensure Python 3.9+ and MySQL Server 8.0+ are installed.



Install Python packages:

pip install -r requirements.txt



Configure MySQL:





Create a database named todo_db:

CREATE DATABASE todo_db;



Create a MySQL user (or use defaults: todo_user, todo_password):

CREATE USER 'todo_user'@'%' IDENTIFIED BY 'todo_password';
GRANT ALL PRIVILEGES ON todo_db.* TO 'todo_user'@'%';
FLUSH PRIVILEGES;



Update main.py with your MySQL credentials if different from the defaults.



Run the Application:

uvicorn main:app --host 0.0.0.0 --port 8000





Access the application at:

http://localhost:8000/static/signup.html



Stop the Application:





Press Ctrl+C in the terminal.

Project Structure

The project is organized as follows:

todo-list/
├── frontend/                    # Frontend assets
│   ├── index.html              # Task management page
│   ├── signup.html             # Sign-up page
│   ├── login.html              # Login page
│   ├── styles.css              # CSS styles for the UI
│   └── script.js               # JavaScript for client-side logic and API requests
├── Dockerfile                  # Docker configuration for the backend
├── docker-compose.yml          # Orchestrates backend and MySQL services
├── main.py                     # FastAPI backend code (API routes, authentication, database logic)
├── requirements.txt            # Python dependencies for the backend
├── README.md                   # Project documentation and setup instructions
└── ProjectSummary.md           # Detailed project summary

Troubleshooting

Common issues and their solutions:





MySQL Connection Issues:





If the backend logs show Can't connect to MySQL server, ensure the MySQL service is fully started. Wait 10-20 seconds after running docker compose up and retry.



Verify the MySQL credentials in docker-compose.yml (MYSQL_USER, MYSQL_PASSWORD).



Check if port 3307 is free:

netstat -aon | findstr :3307



Port Conflicts:





If port 8000 (backend) or 3307 (MySQL) is in use, stop conflicting services or update docker-compose.yml to use different ports (e.g., 8001:8000, 3308:3306).



JWT Errors:





If authentication fails, ensure the SECRET_KEY in main.py is consistent and not changed between deployments.



Check browser console (F12 -> Console) for errors like 401 Unauthorized, which may indicate an invalid or expired token.



Missing Dependencies:





If the backend crashes with errors like ModuleNotFoundError: No module named 'python-multipart', ensure requirements.txt includes python-multipart==0.0.9 and rebuild the Docker image:

docker compose up --build



Frontend Issues:





If pages (signup.html, login.html) fail to load, verify that the frontend/ directory contains all required files (index.html, signup.html, login.html, styles.css, script.js).



Check browser console for errors like Failed to fetch, which may indicate incorrect API endpoints in script.js.

For additional support, refer to the logs:

docker compose logs

Team

The To-Do List application was developed by a collaborative team of dedicated contributors:





Mohamed Abdelrahman



Mohamed Elsayed



Mohamed Ali



Mohamed Oshry



Islam Gamal

Together, the team worked to design, develop, test, and deploy a high-quality application, ensuring a seamless and reliable user experience.

License

This project is licensed under the MIT License. See the LICENSE file for details.