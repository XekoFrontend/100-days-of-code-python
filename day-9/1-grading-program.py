student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91 and student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable" 
    elif student_scores[student] < 71:
        student_grades[student] = "Fail" 

# Testing grade dictionary
# print(student_grades) 

for name in student_grades:
  student = name
  grade = student_grades[name]
  print(f"{student} got {grade} grades.")