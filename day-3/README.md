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

- String

```python
text = "hello world, hello universe"
count_hello = text.count("hello")
print(count_hello)  # Output: 2

count_o = text.count("o")
print(count_o)  # Output: 3

count_l = text.count("l", 0, 10)
print(count_l)  # Output: 2 (chỉ đếm trong "hello wor")
```

- List

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

### 3. Trick Your Brain with the 20min Rule

_**12 Rules to Learn to Code by Dr. Angela Yu**_

Quote:

> As humans, we have a lot of inertia. This can be bad for us - I’m looking at you, “24” box set. However, we can also turn it to our advantage. I found that once I got started coding and making things, I got so absorbed into the project, that I no longer cared about TV, food or sleep. There were quite a few weekends when I coded until sunrise.
>
> So how do we take advantage of this inertia? First, you must understand that task-switching is very difficult. It requires a lot of motivation. If as soon as you get home, you slump on the sofa and switch on the TV, you’ve already lost that evening. This is because the amount of motivation required to task-switch and do something not driven by evolution like eating or sleeping is a Herculean task.
>
> This is why the moment you enter the door and change to a new environment is the most crucial moment. If at this moment, you tell yourself that you are just going to do 20 minutes of coding practice, you will most likely succeed and use your own inertia to end up learning for an hour or more. No brain will perceive a 20-minute task as a lot of effort and you end up tricking your brain to take advantage of your evening.
>
> The next step is to develop a habit.

Vietnamese translation.

> Con người, thường có **xu hướng làm việc theo quán tính (Flow)**. Điều này có thể gây hại cho chúng ta. Tuy nhiên, chúng ta cũng có thể biến nó thành lợi thế của mình. Tôi phát hiện ra rằng một khi bắt đầu lập trình và tạo ra thứ gì đó, tôi trở nên chìm đắm vào dự án đến mức không còn quan tâm đến TV, thức ăn hay giấc ngủ. Có khá nhiều cuối tuần tôi đã lập trình cho đến bình minh.
>
> Vậy làm thế nào để tận dụng được Flow này? Đầu tiên, bạn phải hiểu rằng việc chuyển đổi công việc là rất khó khăn. Nó đòi hỏi rất nhiều động lực. Nếu ngay khi bạn về nhà, bạn lăn ra sofa và bật TV, bạn đã mất một buổi tối. Bởi vì lượng động lực cần thiết để chuyển đổi công việc và làm điều gì đó không được thúc đẩy bởi những việc bản năng như ăn uống hay ngủ nghỉ.
>
> Đó là lý do tại sao khoảnh khắc bạn bước vào cửa và thay đổi môi trường mới là quan trọng nhất. Nếu vào lúc này, bạn tự nhủ rằng bạn **chỉ lập trình trong 20 phút**, bạn sẽ có khả năng thành công và sử dụng quán tính này để cuối cùng tiếp tục trong một giờ hoặc hơn. **Không có bộ não nào cảm thấy một nhiệm vụ 20 phút là quá nhiều công sức và bạn sẽ lừa được bộ não của mình** để tận dụng buổi tối đấy.
>
> **Bước tiếp theo là phát triển một thói quen**.
