# Input a Python list of student heights
# Ex 1: 151 145 179 = 158
# Ex 2: 156 178 165 171 187 = 171
student_heights = input("Enter student height (cm):\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇

# Count total students in the list
total_students = len(student_heights)

# Sum of student heights
sum_height = 0
for height in student_heights:
  # sum_height = sum_height + int(height)
  sum_height += int(height)

average_height = round(sum_height / total_students)

print(f"total height = {sum_height}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")

# Angela's code solution
'''
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

total_student = 0
for student in student_heights:
  total_student += 1
print(f"number of students = {total_student}")

average_height = round(total_height / total_student)
print(f"average height = {average_height}")
'''