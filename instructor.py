from nss_person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first, last, slack, cohort, specialty):
        super().__init__(first, last, slack, cohort)
        self.instructor_specialty = specialty
    
    def assign(self, student, exercise):
        student.current_exercises.append(exercise)






