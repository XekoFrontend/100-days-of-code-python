# 100 Days of Code: Day 5

## Table of Contents

- [Table of Contents](#table-of-contents)
- [A. Main content](#a-main-content)
  - [For Loop](#for-loop)
  - [range()](#range)
- [B. Extra contents](#b-extra-contents)
  - [random.shuffle()](#randomshuffle)
  - [Find all item locations](#find-all-item-locations)

## A. Main content

### For Loop

- Example 1: Total

```python
student_heights = [151, 145, 179]
sum_height = 0
for height in student_heights:
  sum_height += int(height)
print(sum_height) # 475
```

- Example 2: Highest number

```python
student_score = [78, 55, 91, 64, 89]
highest_score = 0
# to loop through each of the scores in the list of student_scores.
for score in student_scores:
  score = int(score)
  # If the current score > the previously had, we set tge highest_score to that current score.
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")
```

- Example 3:

```python
# Ex: 78 65 89 86 55 91 64 89
student_scores = input("Enter the list of student scores:\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
```

### range()

`range(star, stop [, step])`
Hàm trả về một đối tượng range, không phải là một danh sách các số nguyên. Để chuyển đổi đối tượng range sang một danh sách, bạn có thể sử dụng hàm `list()`.

```python
numbers = list(range(1, 6, 2))
print(numbers) #[1, 3, 5]
```

## B. Extra contents

### random.shuffle()

Dùng để đảo lộn vị trí các phần tử trong một list.

```python
import random

new_list = ['x', 'L', 'm', 'a', '#', '%', '3', '4']
random.shuffle(new_list)
print(new_list) #['4', '%', '#', 'a', 'x', 'm', 'L', '3']
```

### Find all item locations

I solved another student's assignment on [facebook](https://www.facebook.com/groups/790427278627368/permalink/1172642740405818/).

```python
# Tìm tất cả vị trí của Táo
hoa_qua = ["Lê", "táo", "táo", "chuối", "táo", "xoài", "nho", "táo", "táo"]
index = 0
for fruit in hoa_qua:
  if fruit == "táo":
    print(index)
  index += 1
```
