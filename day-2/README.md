# 100 Days of Code: Day 2

## Table of Contents

- [Data types](#data-types)
  - [String](#string)
  - [Integer](#integer)
  - [Float](#float)
  - [Boolean](#boolean)
- [Operations](#operations)
- [Type Conversion](#type-conversion)
- [f-string](#f-string)

## Data types

### String

- Subscript:

  - `print("Hello"[0])` # H
  - `print("Hello"[4])` # o
  - `print("Hello"[-1])` # o

- Concatenation:
  - `print("123" + "world")` # 123world

### Integer

- Example:
  - `print(123_000 + 1)` # 123001

### Float

- Example:
  - `3.14159`

### Boolean

- Always begin with a capital T or F:
  - `True`
  - `False`

## Operations

PEMDA, left to right (Thứ tự ưu tiên trong toán học, từ trái sang phải)

- () (ngoặc đơn)
- 2 \* 3 # 8 (số mũ, lũy thừa)
- 3 \* 2 (nhân)
- 6 / 3 (chia)
- 3 + 5 (cộng)
- 7 - 4 (trừ)
- 8 // 3 # 2 (Phép chia không lấy số dư)
- score += 1 (tăng giá trị của score thêm 1)
- score -= 1 (giảm giá trị của score đi 1)
- score \*= 1 (nhân giá trị của score với 1)
- score /= 1 (chia giá trị của score cho 1)

## Type Conversion

- Show data type:
  ```python
  a = "5"
  print(type(a))  # <class 'str'>
  ```
