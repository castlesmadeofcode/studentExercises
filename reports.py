import sqlite3


class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort


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

            for student in all_students:
                print(f'{student.first_name} {student.last_name} is in {student.cohort}')

reports = StudentExerciseReports()
reports.all_students()