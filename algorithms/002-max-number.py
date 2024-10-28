import random
numbers = []
max_stop = random.randint(10, 20)
for length in range (max_stop - 1):          # Thực hiện độ dài danh sách ngẫu nhiên
  number_random = random.randint(1,max_stop) # Tạo số ngẫu nhiên trong phạm vi được chỉ định.
  numbers.append(number_random)
print(numbers)

# Find the largest number in the list.
max_number = numbers[0]     # Giả sử phần tử đầu tiên là lớn nhất
for number in numbers:
    if number > max_number: # Nếu phần tử hiện tại lớn hơn max_number thì
        max_number = number # Gán giá trị của phần tử hiện tại cho max_number.
print(max_number)

'''
Giải thích:
max_number = numbers[0]: Gán phần tử đầu tiên của danh sách cho biến max_number để bắt đầu so sánh.
for number in numbers:: Vòng lặp duyệt qua từng phần tử trong danh sách.
if number > max_number:: Nếu phần tử hiện tại lớn hơn max_number thì gán giá trị của phần tử hiện tại cho max_number.
'''

# Dùng hàm 'max()'
# max_number = max(numbers)