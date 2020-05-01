
class Cohort: 
    def __init__(self, cohort):
        self.cohort_name = cohort
        self.cohort_students = []
        self.cohort_instructors = [] 

    def __repr__(self):
        return f'{self.cohort_name}'
