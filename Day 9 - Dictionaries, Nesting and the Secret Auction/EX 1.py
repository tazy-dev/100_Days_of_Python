"""
A Grading Program
"""


def scoreToGrade(grade:int)->str :
    """
Convert a student score to a grade
"""
    if grade > 90 :
        return "Outstanding"
    if (grade > 80 and grade <=90) :
        return "Exceeds Expectations"
    if (grade > 70 and grade <=80) :
        return "Acceptable"
    return "Fails"
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for score in student_scores:
    student_grades[score]= scoreToGrade(student_scores[score])
    

# 🚨 Don't change the code below 👇
print(student_grades)

