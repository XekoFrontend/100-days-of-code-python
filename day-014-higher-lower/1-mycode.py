import art, game_data, random
print(art.logo)

release_A = []
release_B = []
score = 0

# Random question
def question(order):
    """ Random question"""
    data = game_data.data
    random_comics = random.randint(0, len(data) - 1)
    release = game_data.data[random_comics]['release']    
    # Save release amount to temps
    if order == 'Compare A':
        release_A.append(release)
    else:
        release_B.append(release)
    # Show the questions
    select_comics = data[random_comics]
    return f"{order}: {select_comics['name']} {release}, from {select_comics['country']}.\n{select_comics['description']}"

# So sánh sô lượng phát hành
def compare_release(choice):
    """ Compare release amount and show notification """
    if choice == "A" and release_A > release_B:
        return 1
    elif choice == "B" and release_A < release_B:
        return 1
    else:
        return 0


question_A = question(order='Compare A')

game_over = False
while not game_over:
    print(question_A)
    print(art.vs)
    question_B = question(order='Compare B')
    print(question_B)

    choice = input("Which one sells better? Type 'A' or 'B': ").capitalize()
    compare_result = compare_release(choice)
    # Nếu đúng thì cộng 1 điểm và tiếp tục game, nếu sai thì thoát game.
    if compare_result == 1:
        score += 1
        print(f"You're right! Current score: {score}")
        question_A = question_B
    else:
        print(f"Sorry, that's wrong.Final score: {score}")
        game_over = True


# output = compare_release(choice)
# print(output)




# TODO:
# bug 2 câu A - B không được giống nhau
# Nếu đúng câu B thành A (tham khảo thuật toán sắp xếp)
# bug sau khi gán A = B thì không dùng được phép so sánh. Cần xem lại phần gán câu hỏi. Xem cả trong function
# DONE: Nếu đúng + 1 điểm, sai thì thông báo rồi hỏi có chơi tiếp không?