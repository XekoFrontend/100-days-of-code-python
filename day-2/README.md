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

## Data types (Kiểu dữ liệu)

### 1. String (Chuỗi ký tự)

- Subscript (Chỉ số):

  - `print("Hello"[0])` # H (lấy ký tự đầu tiên)
  - `print("Hello"[4])` # o (lấy ký tự thứ 5)
  - `print("Hello"[-1])` # o (lấy ký tự cuối cùng)

- Concatenation (Nối chuỗi):
  - `print("123" + "world")` # 123world (nối hai chuỗi lại với nhau)

### 2. Integer (Số nguyên)

- Example (Ví dụ):
  - `print(123_000 + 1)` # 123001 (dấu gạch dưới chỉ để dễ đọc, không ảnh hưởng đến giá trị)

### 3. Float

- Example (Ví dụ):
  - `3.14159` (số thập phân)

### 4. Boolean (Giá trị đúng/sai)

- Always begin with a capital T or F (Luôn bắt đầu bằng chữ in hoa T hoặc F):
  - `True` (đúng)
  - `False` (sai)

## Type convert function (Hàm chuyển đổi kiểu dữ liệu):

- `type()` (Cho biết dữ liệu thuộc dạng nào)

  ```python
  a = "5"
   print(type(a)) # <class 'int'>
  ```

- Type convert function
  - `str()` (chuyển sang chuỗi)
  - `int()` (chuyển sang số nguyên)
  - `float()` (chuyển sang số thập phân)

## Operations (Phép toán)

PEMDA, left to right (Thứ tự ưu tiên trong toán học)

- `()` (ngoặc đơn)
- `2 ** 3` # 8 (số mũ, lũy thừa)
- `3 * 2` (nhân)
- `6 / 3` (chia)
- `3 + 5` (cộng)
- `7 - 4` (trừ)

- `8 // 3` # 2 (Phép chia không lấy số dư)

Augmented assignment (phép gán toán học)

- `score += 1` (tăng giá trị của score thêm 1)
- `score -= 1` (giảm giá trị của score đi 1)
- `score *= 1` (nhân giá trị của score với 1)
- `score /= 1` (chia giá trị của score cho 1)

## f-string

f-string giúp chèn biến và biểu thức Python vào trong chuỗi một cách dễ dàng và trực quan.

```python
name = "Alice"
age = 30

# Sử dụng f-string
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.
```

```python
calculation = f"The sum of 2 and 3 is {2 + 3}."
print(calculation) # Output: The sum of 2 and 3 is 5.
```
