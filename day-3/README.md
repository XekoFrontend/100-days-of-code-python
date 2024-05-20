# 100 Days of Code: Day 3

## Table of Contents

- [Conditional statements](#conditional-statements)
  - [If else](#1-if-else)

## Conditional statements

### 1. If else

```python
if height >= 120:
  print("Welcome!")
else:
  print("Go out!")
```

### 2. Nested if

- [<u>Example code: Leap Year Exercise</u>](./leap-year.py)

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

- [<u>Example code: Rollercoaster</u>](./elif-rollercoaster.py)

### Logical operators

#### Comparison Operators

- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to
- `==` Equal to
- `!=` Not equal to

## Code blocks

## Scope

### Global

### Local
