from nss_person import NSSPerson

class Student(NSSPerson):
    def __init__(self, first, last, slack, cohort):
        super().__init__(first, last, slack, cohort)
        self.current_exercises = []

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


