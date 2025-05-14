Project Summary

Project Purpose

The To-Do List application is a robust, secure, and intuitive web-based platform designed to empower users to manage their daily tasks with ease and efficiency. It provides a seamless experience for individuals to register, authenticate, and organize their tasks through a clean, accessible interface. The application serves both practical and educational purposes: it offers a real-world solution for personal task management while showcasing advanced software development practices. By integrating containerization, microservices orchestration, and secure authentication, the project demonstrates proficiency in full-stack development, modern DevOps workflows, and scalable system design. Developed as a collaborative effort, the To-Do List application reflects industry-standard techniques, making it an exemplary model for building reliable, user-centric web applications.

Features

The To-Do List application is equipped with a comprehensive set of features to enhance user productivity and ensure a secure, engaging experience:





User Registration (Sign Up): Enables users to create personalized accounts by submitting a unique username and password. Passwords are securely hashed using the bcrypt algorithm and stored in a MySQL database, ensuring robust protection against unauthorized access. The registration process is streamlined, with clear feedback for errors like duplicate usernames or invalid inputs.



User Authentication (Login): Provides secure access through JSON Web Tokens (JWT). Users authenticate with their credentials, receiving a JWT token that is stored client-side and used to access protected API endpoints. The login system is designed for reliability, with error handling for invalid credentials and session management to maintain user privacy.



Task Management:





Create Task: Allows authenticated users to add tasks with a mandatory title and an optional description. Tasks are stored in the MySQL database, associated with the user's unique ID, ensuring data isolation and personalized access.



View Tasks: Retrieves and displays a list of tasks specific to the logged-in user. The frontend renders tasks dynamically, with support for pagination to handle large task lists efficiently, enhancing performance and usability.



Delete Task: Enables users to remove unwanted tasks with a single action. Deletions are instantly reflected in the database and user interface, maintaining a consistent and responsive experience.



Responsive Design: The frontend, built with HTML, CSS, and JavaScript, adapts seamlessly to various screen sizes, ensuring accessibility on desktops, tablets, and smartphones. The interface prioritizes simplicity and clarity, making task management intuitive for all users.



Robust Error Handling: The application handles edge cases gracefully, providing meaningful feedback for scenarios such as network failures, database errors, or invalid user inputs. This ensures a smooth user experience even under unexpected conditions.



Secure Data Management: All user data, including credentials and tasks, is managed securely with encryption and validation, adhering to best practices for data privacy and integrity.

Technology Stack

The To-Do List application leverages a modern, high-performance technology stack to deliver a scalable and maintainable solution:





Backend:





FastAPI (Python): A lightweight, asynchronous framework chosen for its speed, automatic OpenAPI documentation, and support for building RESTful APIs. FastAPI powers the application's core logic, handling user authentication, task CRUD operations, and API routing.



Uvicorn: An ASGI server that runs the FastAPI application, providing efficient request handling and support for concurrent connections.



Database:





MySQL 8.0: A relational database selected for its reliability, performance, and support for structured data. MySQL stores user accounts (username, hashed password) and tasks (title, description, user ID) with foreign key constraints to ensure referential integrity.



Frontend:





HTML, CSS, JavaScript: A minimal yet powerful frontend stack that delivers a responsive, client-side interface. JavaScript drives dynamic interactions, using AJAX to communicate with the backend API and update the UI in real-time.



Static File Serving: FastAPI's StaticFiles module serves frontend assets from the frontend/ directory under the /static endpoint, ensuring fast and reliable access to HTML, CSS, and JavaScript files.



Containerization:





Docker: Encapsulates the application (backend, dependencies, and frontend) into a portable container based on the python:3.9-slim image. Docker ensures consistency across development, testing, and production environments, minimizing "it works on my machine" issues.



Dockerfile: Defines a streamlined build process, installing dependencies from requirements.txt, copying application files, and configuring a non-root user for enhanced security.



Orchestration:





Docker Compose: Orchestrates the application's services (FastAPI backend and MySQL database) within a custom bridge network (app-network). It manages environment variables, port mappings (e.g., MySQL on 3307:3306), and health checks to ensure proper startup and communication between services.



Authentication and Security:





JWT (PyJWT): Implements stateless authentication by generating and validating JSON Web Tokens, enabling secure access to protected routes without server-side session storage.



bcrypt (passlib): Secures user passwords through strong hashing, protecting against brute-force attacks and data breaches.



MySQL Connector: Provides a reliable interface for the FastAPI backend to interact with the MySQL database, supporting secure queries and transactions.



Additional Libraries:





python-multipart: Facilitates parsing of form data for authentication endpoints, enabling support for OAuth2PasswordRequestForm in login requests.



aiofiles: Enhances performance by enabling asynchronous file operations for serving static frontend files.

Team

The To-Do List application was developed by a dedicated and collaborative team, combining their expertise to deliver a high-quality product:





Mohamed Abdelrahman



Mohamed Elsayed



Mohamed Ali



Mohamed Oshry



Islam Gamal

Together, the team contributed to all aspects of the project, from design and development to testing and deployment, ensuring a cohesive and polished final application.

Additional Notes





Source Code: The project is hosted on GitHub at https://github.com/Muhamed-Abdelrahman/todo-list-docker, providing full access to the codebase, documentation, and version history.



Docker Image: A pre-built Docker image is available on DockerHub at https://hub.docker.com/r/dracola1/todo-list, enabling easy deployment with minimal setup.



Deployment Instructions: To run the application locally, clone the repository, navigate to the project directory, and execute docker compose up --build. The application will be accessible at http://localhost:8000/static/signup.html. Ensure Docker and Docker Compose are installed.



Maintenance: The application is designed for easy maintenance, with modular code, clear documentation, and automated dependency management via requirements.txt. Regular updates to the Docker image ensure compatibility with the latest library versions.



Future Enhancements: Planned improvements include:





Task prioritization and due dates for enhanced task management.



Support for task categories or tags to improve organization.



Integration with a frontend framework (e.g., React or Vue.js) for a more interactive UI.



Email notifications for task reminders or account verification.



CI/CD pipelines for automated testing and deployment.