# 100 Days of Code: Day 3

## Table of Contents

- [Conditional statements](#conditional-statements)
  - [If else](#1-if-else)
  - [Nested if](#2-nested-if)
  - [elif](#3-elif)
  - [Multiple if vs elif](#4-multiple-if-vs-elif)
- [Logical operators](#logical-operators)
- [Comparison Operators](#comparison-operators)
- [Bonus](#b-bonus)
  - [count()](#1-count)
  - [.lower(), .upper(), .title()](#2-lower-upper-title)

## A. Main content

## Conditional statements

### 1. If else

```python
if height >= 120:
  print("Welcome!")
else:
  print("Go out!")
```

### 2. Nested if

- [<u>Example code: Leap Year Exercise</u>](./4-leap-year.py)

  - [<u>Leap Year Flow Chart</u>](./4-leap-year-flow-chart.jpg)

### 3. elif

```python
if height > 120:
  age = int(input("How old are you?\n"))
  if age < 12:
    print('Your ticket costs $5.')
  elif age > 18:
    print("Your ticket costs $12.")
  else:
    print("Your ticket costs $7.")
else:
  print("You can't ride 😒")
```

### 4. Multiple if **vs** elif

| Multiple if                                                                                                 | elif                                                                                             |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Mỗi điều kiện được kiểm tra độc lập. Nhiều điều kiện có thể đúng và các khối mã tương ứng sẽ được thực thi. | Các điều kiện được kiểm tra tuần tự. Khi một điều kiện đúng, các điều kiện còn lại sẽ bị bỏ qua. |

```python
# Variable keeps track of the ongoing price.
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
```

## Logical operators

- `and`
- `or`
- `not`

## Comparison Operators

- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to
- `==` Equal to
- `!=` Not equal to

## B. Bonus

### 1. count()

> Hàm count() trong Python được sử dụng để đếm số lần một giá trị xuất hiện trong một chuỗi (string) hoặc danh sách (list).

1. String

```python
text = "hello world, hello universe"
count_hello = text.count("hello")
print(count_hello)  # Output: 2

count_o = text.count("o")
print(count_o)  # Output: 3

count_l = text.count("l", 0, 10)
print(count_l)  # Output: 2 (chỉ đếm trong "hello wor")
```

2. List

```python
numbers = [1, 2, 3, 4, 1, 2, 1]
count_1 = numbers.count(1)
print(count_1)  # Output: 3
```

### 2. .lower(), .upper(), .title()

```python
"KiloMeter".lower()  # kilometer
"KiloMeter".upper()  # KILOMETER
"KilOMeTEr".title()  # Kilometer
```
