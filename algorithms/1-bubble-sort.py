# https://g.co/gemini/share/acbb90f9ce97
# https://chatgpt.com/share/67052acd-a3cc-8004-a630-e38102ade9a6

print("Thuật toán Bubble sort, săp xếp theo thứ tự.")

num_list=[3,5,1,8,4,7,9,0,6,2]

print("Danh sách ban đầu:", num_list)

# Lặp qua tất cả các phần tử trong danh sách
for i in range(len(num_list) - 1):  
  # Vòng lặp bên trong các phần tử  còn lại của danh sách ngoài i
  for j in range(len(num_list) - 1 - i):
    # Tìm phần tử nhỏ nhất để so sánh và đổi chỗ
    # Nếu số phía trước lớn hơn số phía sau, hoán đổi
    if num_list[j] > num_list[j+1]:
      # Hoán đổi vị trí
      num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

print("Từ nhỏ đến lớn   :", num_list)
