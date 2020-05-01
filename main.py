# import the classes you need, and implement the following logic.
from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

# Create 4, or more, exercises.
html_exercise = Exercise("Fun With HTML", "HTML")
css_exercise = Exercise("Fun With CSS", "CSS")
javascript_exercise = Exercise("Fun With JavaScript", "JavaScript")
python_exercise = Exercise("Fun With Python", "Python")

# Create 3, or more, cohorts.
cohort_38 = Cohort("Cohort 38")
cohort_13 = Cohort("Cohort 13")
cohort_100 = Cohort("Cohort 100")

# Create 4, or more, students and assign them to one of the cohorts.
castle = Student("Castle", "Crawford", "@castle", "Cohort 38")
wazowski = Student("Mike", "Wazowski", "@wazowski", "Cohort 13")
steve = Student("Steve", "Jobs", "@steve", "Cohort 100")
bill= Student("Bill", "Gates", "@gates", "Cohort 100")

# Create 3, or more, instructors and assign them to one of the cohorts.
andy = Instructor("Andy", "Bobandy", "@bobandy", "Cohort 38", "Bringing the pain")
nill= Instructor("Nill", "Gates", "@therealgates", "Cohort 100", "Clapping loudly")
jim= Instructor("Jim", "Bob", "@skeeter", "Cohort 13", "Drinking beer")

# Have each instructor assign 2 exercises to each of the students.

andy.assign(castle, python_exercise)
andy.assign(castle, javascript_exercise)

nill.assign(wazowski, css_exercise)
nill.assign(wazowski, html_exercise)

jim.assign(steve, javascript_exercise)
jim.assign(steve, python_exercise)

jim.assign(bill, html_exercise)
jim.assign(bill, javascript_exercise)






