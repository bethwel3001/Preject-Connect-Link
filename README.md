Project Connect-Link
This is a web app that connects youths/volunterrs to opportunities and vice versa
Built in HTML, CSS, JAVASCRIPT for frontend and Python, Flask for backend with MySql for the database part, this project was agamechanger for my journey as an apprentice software engineer
sample imaged
![image](https://github.com/user-attachments/assets/758acdf9-5bb1-41be-94c7-2caf4c323b3c)


![image](https://github.com/user-attachments/assets/5ce21e19-ac5d-47f2-8a3b-52d1cb3fb6c8)  ![image](https://github.com/user-attachments/assets/37a20ac1-8b79-4276-b083-469a8ba1f4f5)

![image](https://github.com/user-attachments/assets/25112cda-0bd9-42e1-85fb-a271773d0f81)

**Explanation of Each Folder/File**
1. app.py:
The main entry point that initializes the Flask app and runs the server.

2. config.py:
Stores app configurations (e.g., database URL, secret keys).

3. /connectlink/:
Contains backend logic like models, routes, forms, and utility functions. This is the core package of the application.

4. /templates/:
HTML templates using Jinja2 for rendering dynamic content.
base.html will serve as the base layout for other pages (like a master template with a consistent navbar and footer).

5. /static/:
Holds static files (CSS, JavaScript, and images).
This folder ensures that frontend assets are served efficiently.

6. /instance/:
Stores instance-specific files, such as SQLite DB (for local testing) and config files not intended for version control.

7. /tests/:
Contains all the unit and integration tests to ensure the application works as expected.

8. migrations/:
If you use Flask-Migrate for handling database migrations, this folder stores migration scripts.

9. requirements.txt:
Contains all the Python dependencies needed to run the project (e.g., Flask, SQLAlchemy, Flask-WTF).
10. .env:
Stores sensitive environment variables (e.g., secret keys, API tokens).

11. /docs/:
Useful for documenting your API endpoints and providing usage instructions for future developers or contributors.

**Technologies Used**
1. Frontend: HTML, CSS, JavaScript
2. Backend: Python *Flask*
3. Database: SQLite (for local testing) / PostgreSQL or *MySQL* (for production) 
4. Authentication: Flask-Login
5. Forms & Validation: Flask-WTF
6. Migrations: Flask-Migrate

**Headaches to Expect 😅**
1. Authentication issues: Handling login sessions and password encryption securely.
2. Database management: Ensuring migrations run smoothly during development and deployment.
3. Frontend-backend sync: Making sure data flows seamlessly between the two.
4. Form validation quirks: Client-side vs. server-side validation conflicts.
5. Deployment troubles: Configuring the environment and database correctly during deployment to platforms like Netlify or Heroku.
