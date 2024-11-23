# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Enter a two-digit number : ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
numb1 = int(two_digit_number[0])
numb2 = int(two_digit_number[1])
sum = numb1 + numb2

print("The sum of the two numbers is: " + str(sum))
