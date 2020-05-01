import sqlite3
from student import Student
from instructor import Instructor

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/nscc1/workspace/python/student/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohortId,
                c.cohort_name
            from Student s
            join Cohort c on s.cohortId = c.Id
            order by s.cohortId
            """)

            all_students = db_cursor.fetchall()
            [print(s) for s in all_students]

            # for student in all_students:
            #     print(student)

    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[6], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.cohortId,
                i.instructor_specialty,
                c.cohort_name
            from Instructor i
            join Cohort c on i.cohortId = c.Id
            order by i.cohortId
            """)

            all_instructors = db_cursor.fetchall()
            [print(i) for i in all_instructors]

            # for instructor in all_instructors:
            #     print(instructor)


reports = StudentExerciseReports()
# reports.all_students()
# reports.all_instructors()