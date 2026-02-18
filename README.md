# Student Enrollment Web Application

A full-stack web application built using Flask and MySQL to manage students, courses, and enrollments.

## Features

- Add and manage students
- Add and manage courses
- Enroll students in courses
- View relational enrollment data using JOIN queries
- MySQL database integration
- Flask backend with dynamic HTML rendering

## Tech Stack

- Python 3
- Flask
- MySQL
- HTML
- Virtual Environment (venv)

## Project Structure

student_enrollment_app/
│
├── app.py
├── db_connection.py
├── templates/
│ └── index.html
├── requirements.txt
└── .gitignore


## ⚙️ Installation

1. Clone the repository:
git clone https://github.com/Piyush-Rajbanshi/student-enrollment-flask-app.git

2. Navigate into the folder:
cd student-enrollment-flask-app

3. Create virtual environment:
python3 -m venv venv
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Configure your MySQL database in `db_connection.py`.

6. Run the application:
python app.py


7. Open in browser:
http://127.0.0.1:5000


## What I Learned

- Building relational databases with foreign key constraints
- Integrating MySQL with Python
- Developing a Flask web application
- Handling POST requests and rendering dynamic data
- Using virtual environments for dependency management

---

Developed by Piyush Rajbanshi


