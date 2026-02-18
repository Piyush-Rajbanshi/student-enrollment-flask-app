from flask import Flask, render_template, request, redirect
from db_connection import get_connection

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT e.enrollment_id, s.full_name, c.course_name, e.enrollment_date
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id
    """)

    enrollments = cursor.fetchall()
    conn.close()

    return render_template("index.html", enrollments=enrollments)


@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form["name"]
    email = request.form["email"]
    year = request.form["year"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (full_name, email, enrollment_year) VALUES (%s, %s, %s)",
        (name, email, year)
    )
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/add_course", methods=["POST"])
def add_course():
    name = request.form["course_name"]
    duration = request.form["duration"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses (course_name, course_duration_months) VALUES (%s, %s)",
        (name, duration)
    )
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/enroll", methods=["POST"])
def enroll():
    student_id = request.form["student_id"]
    course_id = request.form["course_id"]
    date = request.form["date"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)",
        (student_id, course_id, date)
    )
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
