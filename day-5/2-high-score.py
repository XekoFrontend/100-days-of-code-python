# Input a list of student scores
# Ex: 78 65 89 86 55 91 64 89 = 91
student_scores = input("Enter the list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# Write your code below this row 👇

# Angela's code solution
highest_score = 0
# to loop through each of the scores in the list of student_scores.
for score in student_scores:
  score = int(score)
  # If the current score > the previously had, we set tge highest_score to that current score. 
  if score > highest_score:
    highest_score = score
    
print(f"The highest score in the class is: {highest_score}")