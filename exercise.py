# You must define a type for representing an exercise in code.
#  An exercise can be assigned to many students.

# Name of exercise
# Language of exercise (JavaScript, Python, CSharp, etc.)

class Exercise:
    def __init__(self, name, language):
        self.exercise_name = name
        self.exercise_language = language

    def __repr__(self):
        return f'{self.exercise_name} {self.exercise_language}'

        