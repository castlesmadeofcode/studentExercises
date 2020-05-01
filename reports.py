import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

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

    def all_cohorts(self):

        """Retrieve all cohorts with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.cohort_name
            from Cohort i
            """)

            all_cohorts = db_cursor.fetchall()
            [print(i) for i in all_cohorts]

            # for cohort in all_cohorts:
            #     print(cohort)

    def all_exercises(self):

        """Retrieve all exercises with the exercise name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.exercise_name,
                i.exercise_language
            from Exercise i
            """)

            all_exercises = db_cursor.fetchall()
            [print(i) for i in all_exercises]

            # for exercise in all_exercises:
            #     print(exercise)


    def all_javascript_exercises(self):

        """Retrieve all exercises with the exercise name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.exercise_name,
                i.exercise_language
            from Exercise i
            where i.exercise_language = 'JavaScript'
            """)

            all_exercises = db_cursor.fetchall()
            [print(i) for i in all_exercises]

            # for exercise in all_exercises:
            #     print(exercise)

    def all_python_exercises(self):

        """Retrieve all exercises with the exercise name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.exercise_name,
                i.exercise_language
            from Exercise i
            where i.exercise_language = 'Python'
            """)

            all_exercises = db_cursor.fetchall()
            [print(i) for i in all_exercises]

            # for exercise in all_exercises:
            #     print(exercise)




reports = StudentExerciseReports()
# reports.all_students()
# reports.all_instructors()
# reports.all_cohorts()
# reports.all_exercises()
# reports.all_javascript_exercises()
# reports.all_python_exercises()
