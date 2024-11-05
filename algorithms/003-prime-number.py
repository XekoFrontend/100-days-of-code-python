# Đoạn code bên dưới có áp dụng phép lũy thừa để tính căn bậc hai trong toán học (num ** 0.5)
# https://chatgpt.com/share/6728bb5e-b800-8004-8a01-b552d4b5e215

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(n=number):
    print(f"{number} là số nguyên tố.")
else:
    print(f"{number} không phải là số nguyên tố.")