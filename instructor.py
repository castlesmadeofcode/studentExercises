# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student
from student import Student

class Instructor:
    def __init__(self, first, last, slack, cohort, specialty):
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.instructor_cohort = cohort
        self.instructor_specialty = specialty
    
    def assign_exercise(self):
        pass



# new_instructor = Instructor("bob", "jim", "bobjim", 38, "fun")
# new_instructor.assign_exercise("do it")


