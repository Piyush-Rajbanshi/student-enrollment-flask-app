from db_connection import get_connection

def add_student():
    name = input("Full name: ")
    email = input("Email: ")
    year = input("Enrollment year: ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students (full_name, email, enrollment_year)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, email, year))
    conn.commit()

    conn.close()
    print("Student added successfully")


def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n--- Students List ---")
    for s in students:
        print(s)

    conn.close()


def update_student_email():
    student_id = input("Student ID: ")
    new_email = input("New email: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET email = %s WHERE student_id = %s",
        (new_email, student_id)
    )
    conn.commit()

    conn.close()
    print("✏️ Email updated")


def delete_student():
    student_id = input("Student ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = %s",
        (student_id,)
    )
    conn.commit()

    conn.close()
    print("Student deleted")

def add_course():
    name = input("Course name: ")
    duration = input("Course duration (months): ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO courses (course_name, course_duration_month)
    VALUES (%s, %s)
    """
    cursor.execute(query, (name, duration))
    conn.commit()
    conn.close()

    print("Course added successfully")


def view_courses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    print("\n--- Courses List ---")
    for c in courses:
        print(c)

    conn.close()


def delete_course():
    course_id = input("Course ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM courses WHERE course_id = %s",
        (course_id,)
    )
    conn.commit()
    conn.close()

    print("Course deleted")

def enroll_student():
    student_id = input("Student ID: ")
    course_id = input("Course ID: ")
    enrollment_date = input("Enrollment date (YYYY-MM-DD): ")

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO enrollments (student_id, course_id, enrollment_date)
    VALUES (%s, %s, %s)
    """

    try:
        cursor.execute(query, (student_id, course_id, enrollment_date))
        conn.commit()
        print("Student enrolled successfully")
    except Exception as e:
        print("Error:", e)

    conn.close()


def view_enrollments():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT e.enrollment_id, s.full_name, c.course_name, e.enrollment_date
    FROM enrollments e
    JOIN students s ON e.student_id = s.student_id
    JOIN courses c ON e.course_id = c.course_id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n--- Enrollment List ---")
    for r in results:
        print(r)

    conn.close()


def delete_enrollment():
    enrollment_id = input("Enrollment ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM enrollments WHERE enrollment_id = %s",
        (enrollment_id,)
    )
    conn.commit()
    conn.close()

    print("Enrollment deleted")
