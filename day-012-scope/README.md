# 100 Days of Code: Day 12 - Scope: Number Guessing Game

## Table of Contents

- [A. Main contents](#a-main-contents)
  - [I. Scope](#i-scope)
    - [1. Local Scope](#1-local-scope)
    - [2. Block Scope](#2-block-scope)
    - [3. Prime number checker](#3-prime-number-checker)


- [B. Extra contents](#b-extra-contents)

## A. Main contents

### I. Scope

#### 1. Local Scope

If you create a variable within a function, then it's only available within that function.

#### 2. Block Scope

But if you create a variable within an ***if block, or a while loop, or a for loop or anything that has the indentation and the colon***, then that does not count as creating a separate local scope.\
Về cơ bản bất kỳ khối mã như: `if`, `for`, `while` khi thụt lề vẫn có cùng phạm vi như hàm bao quanh hoặc nếu không thì sẽ tính là global scope.

#### 3. Prime number checker

Mình chỉ cố gắng tìm cách để đoạn [code của mình](./1-prime-number-mycode.py) có thể chạy tuy nhiên mình cảm thấy không ổn lắm nên tham khảo từ Chat GPT và một lần nữa việc học toán tạo ra sự khác biệt.\
Ban đầu ý tưởng của 
Đoạn code bên dưới áp dụng *'căn bậc hai'* trong toán học. [Reference Chat GPT](https://chatgpt.com/share/6728bb5e-b800-8004-8a01-b552d4b5e215)

```python
def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

num = int(input("Enter a number: "))
output = is_prime(num)
print(output)
```




## B. Extra contents