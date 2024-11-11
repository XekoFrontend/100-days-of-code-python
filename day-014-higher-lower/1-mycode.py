import art, game_data, random
print(art.logo)

release_A = []
release_B = []

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
    """ Compare relase amout and show notification """
    if choice == "A" and release_A > release_B:
        print("You're right! Current score:")
    elif choice == "B" and release_A < release_B:
        print("You're right! Current score:")
    else:
        print("Sorry, that's wrong.Final score: ")

question_A = question(order='Compare A')
print(question_A)
print(art.vs)
question_B = question(order='Compare B')
print(question_B)

choice = input("Which one sells better? Type 'A' or 'B': ").capitalize()
compare_release(choice)


# output = compare_release(choice)
# print(output)




# TODO:
# bug 2 câu A - B không được giống nhau
# Nếu đúng câu B thành A (tham khảo thuật toán sắp xếp)
# Nếu đúng + 1 điểm, sai thì thông báo rồi hỏi có chơi tiếp không?