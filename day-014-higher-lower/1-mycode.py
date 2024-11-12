import art, game_data, random, os

release_amount_temp = []
score = 0

def clear():
    if os.name == 'nt':
        _ = os.system('cls')

# 1. Random question
def question(order):
    """ Random question"""
    DATA = game_data.data
    random_index = random.randint(0, len(DATA) - 1)      
    # Get and Save release amount to temps
    release = DATA[random_index]['release']      
    release_amount_temp.append(release)
    # Show the questions
    select_comics = DATA[random_index]
    return f"\n{order}: {select_comics['name']}, from {select_comics['country']}.\n{select_comics['description']}\n Testing:  {release}"

# 2. Compare release amounts
def compare_release(choice):
    """ Compare release amount and show notification """
    if choice == "A" and release_amount_temp[0] > release_amount_temp[1]:
        return 1
    elif choice == "B" and release_amount_temp[0] < release_amount_temp[1]:
        return 1
    else:
        return 0

# Show the first question
question_A = question(order='Compare A')

game_over = False
while not game_over:
    question_B = question(order='Compare B')    
    print(art.logo)
    print(question_A)
    print(art.vs)       
    print(question_B)

    choice = input("Which one sells better? Type 'A' or 'B': ").capitalize()
    compare_result = compare_release(choice)
    # Nếu đúng thì cộng 1 điểm và tiếp tục game, nếu sai thì thoát game.
    if compare_result == 1:
        score += 1
        print(f"You're right! Current score: {score}")
        clear()
        # Switching questions and release amounts from B to A.    
        question_A = question_B
        release_amount_temp[0] = release_amount_temp [1]
        release_amount_temp.pop()
    else:
        print(f"Sorry, that's wrong.Final score: {score}")
        game_over = True


# output = compare_release(choice)
# print(output)




# TODO:
# bug 2 câu A - B không được giống nhau
# DONE: bug sau khi gán A = B thì không dùng được phép so sánh. Cần xem lại phần gán câu hỏi. Xem cả trong function
# DONE: Nếu đúng câu B thành A (tham khảo thuật toán sắp xếp)
# DONE: Nếu đúng + 1 điểm, sai thì thông báo rồi hỏi có chơi tiếp không?