# You must define a custom type for representing a student in code.
#  A student can only be in one cohort at a time. A student can be 
#  working on many exercises at a time.

# Properties
# First name
# Last name
# Slack handle
# The student's cohort
# The collection of exercises that the student is currently working on

class Student:
    def __init__(self, first, last, slack, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort_number = cohort
        self.current_exercises = []


