# 100 Days of Code: Day 7

For & While Loops
IF / ELSE
Lists
Strings
Range
Modules

## Table of Contents

- [A. Main contents](#a-main-contents)

- [B. Extra contents](#b-extra-contents)

## A. Main contents

### 1. For - Python list documentation

[Google for Education](https://developers.google.com/edu/python/lists#for-and-in)

## B. Extra contents

### 1. Alphabet reverse

Để đảo ngược thứ tự của các phần tử trong danh sách theo thứ tự alphabet, bạn có thể sử dụng phương thức `sort()` cùng với tham số `reverse=True`

```python
a = ['hello', 'hat', 'music', 'control', 'youtube']
a.sort(reverse=True)
print(a)
# Output: ['youtube', 'music', 'hello', 'hat', 'control']
```

### 2. remove(element) vs pop(index)

```python
a = ['hello', 'hat', 'music', 'control', 'youtube']
a.remove("hat")
a.pop(0)
print(a)
# Output: ['music', 'control', 'youtube']
```

### 3.Common error

note that the above methods do not _return_ the modified list, they just modify the original list.

```python
  list = [1, 2, 3]
  print(list.append(4))   ## NO, does not work, append() returns None
  ## Correct pattern:
  list.append(4)
  print(list)  ## [1, 2, 3, 4]
```

### 4. List Slices

List slices là một cách để trích xuất một phần của danh sách trong Python bằng cách sử dụng cú pháp `list[start:stop:step]`

- start: Đây là chỉ mục (index) bắt đầu của phần được trích xuất. Phần tử tại chỉ mục này được bao gồm trong kết quả. Nếu không chỉ định, mặc định là 0 (bắt đầu từ phần tử đầu tiên).
- stop: Đây là chỉ mục kết thúc của phần được trích xuất. Phần tử tại chỉ mục này không được bao gồm trong kết quả. Nếu không chỉ định, mặc định là độ dài của danh sách (lấy tất cả các phần tử đến cuối).
- step: Đây là bước nhảy giữa các phần tử được trích xuất. Mặc định là 1 (lấy các phần tử liên tiếp).

```python
# Tạo một danh sách
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Trích xuất từ chỉ mục 2 đến 5
slice1 = my_list[2:6]
print(slice1)  # Output: [3, 4, 5, 6]

# Trích xuất từ chỉ mục 1 đến hết với bước nhảy 2
slice2 = my_list[1::2]
print(slice2)  # Output: [2, 4, 6, 8, 10]

# Đảo ngược danh sách
reverse_list = my_list[::-1]
print(reverse_list)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

my_list[0:2] = 'z'    # replace [1, 2] with ['z']
print(my_list)        # Output: ['z', 3, 4, 5, 6, 7, 8, 9, 10]
```

### 5. Hangman Flowchart

[Open image](./Solution+-+Hangman+Flowchart+1.png)
