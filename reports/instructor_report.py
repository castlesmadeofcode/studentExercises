import sqlite3


class Instructor():

    def __init__(self, first, last, handle, cohort, specialty):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort
        self.instructor_specialty = specialty

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/nscc1/workspace/python/student/studentexercises.db"

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
reports.all_instructors()