# 100 Days of Code: Day 4

## Table of Contents

- [A. Main content](#a-main-content)
  - [Module](#module)
  - [Random module](#random-module)
  - [List](#list)
    - [Examples](#1-examples)
    - [Nested List](#2-nested-list)
    - [Exercise Review](#3-exercise-review)
- [B. Bonus](#b-bonus)
  - [So sánh 'choice()' và 'random()' trong Python](#so-sanh-choice-va-random-trong-python)
  - [Hàm `split()` trong Python](#ham-split-trong-python)

## A. Main content

### Module

Lợi ích của việc sử dụng module:

- Tổ chức: Chia nhỏ chương trình thành các module giúp bạn dễ dàng quản lý và tìm kiếm các chức năng cần thiết.
- Dễ đọc: Mã được chia thành các module giúp mã dễ đọc và hiểu hơn.
- Tái sử dụng: Bạn có thể sử dụng lại các module trong nhiều chương trình khác nhau, tiết kiệm thời gian và công sức.

Để tạo một module, bạn chỉ cần lưu một tập tin Python với tên .py. Tập tin này có thể chứa các định nghĩa và câu lệnh Python như bất kỳ tập tin Python nào khác. Sau đó, bạn có thể import module này vào các chương trình khác để sử dụng.

```python
import random
```

```python
from math import pi
```

### Random module

Random is a Python module

- Import module

```python
import random
random_integer = random.randint(1, 10) # 1 ... 10
```

- Example random module

```python
random_float = random.random()     # 0.000 ... to 0.9999...
random_float = random.random() * 5 # 0.000 ... to 4.9999...
```

- `random.seed()` Used to generate the same set of random numbers each time the algorithm is executed
- `random.randrange(start,stop[,step])` Given a starting number(start), and the last number(stop), this function is used to generate random numbers with the specified increment(step)
- `random.randint(a,b)` The randint function is used to produce a random integer in the range of a,b

### List

#### 1. Examples

- [Document: More on Lists](https://docs.python.org/3/tutorial/datastructures.html)
- An example that uses most of the list methods:

```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple') # 2
fruits.index('banana') # 3
fruits.index('banana', 4)  # 6 - Find next banana starting at position 4

fruits.reverse() # 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange'
fruits.sort() # 'apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear'

print(fruits[1]) # apple
print(fruits[-1]) # banana

fruits[2] = "Bear" # Rename: 'orange', 'apple', 'Bear', 'banana', 'kiwi', 'apple', 'banana'
fruits.append("watermelon") # Add an item to the end of the list
fruits.extend("them", "mot", "hoac", "nhieu") # 'orange', 'apple', 'Bear', 'banana', 'kiwi', 'apple', 'banana', watermelon, "them", "mot", "hoac", "nhieu"

list.insert(i, x) # i is the index, x is an item
list.copy() #Return a shallow copy of the list.

fruits.pop() # pear - Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
list.remove(x) # Remove the first item from the list whose value is equal to x.
list.clear() #Remove all items from the list.
```

#### 2. Nested List

```python
students = [
    ["Alice", [80, 90, 75], "Toán, Lý, Hóa"],
    ["Bob", [95, 85, 92], "Toán, Sử, Địa"],
    ["Charlie", [70, 82, 68], "Văn, Sử, Lý"],
]
# Lấy tên của học sinh đầu tiên
first_student_name = students[0][0]
print(first_student_name)  # Output: Alice
# Để lấy điểm Toán của học sinh thứ hai
second_student_math_score = students[1][1][0]
print(second_student_math_score)  # Output: 95
# Để lấy danh sách các môn học của học sinh thứ ba
third_student_subjects = students[2][2]
print(third_student_subjects)  # Output: Văn, Sử, Lý
```

#### 3. Exercise Review:

These exercise should be reviewed

- [3-treasure-map.py](./3-treasure-map.py)
- [4-project-rock-paper-scissors](./4-project-rock-paper-scissors.py)

## B. Bonus

### 1. So sánh 'choice()' và 'random()' trong Python

- `random()` khi bạn cần tạo số ngẫu nhiên trong phạm vi nhất định.
  Ex: `random.random()`
- `choice()` khi bạn cần chọn ngẫu nhiên một phần tử từ tập hợp.
  Ex: `random.choice(['a', 'b', 'c'])`

### 2. Hàm `split()` trong Python được sử dụng để chia một chuỗi thành một danh sách các chuỗi con

```python
text = "Hello world! How are you?"
words = text.split(" ", 2)
print(words) # ['Hello', 'world!', 'How are you?']
```

_Lưu ý:_

- Hàm `split()` trả về một danh sách các chuỗi con.
- Nếu separator không được tìm thấy trong chuỗi, chuỗi gốc sẽ được trả về trong một danh sách gồm một phần tử.
- Nếu maxsplit là 0, chuỗi sẽ không bị chia.
