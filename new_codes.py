# import random
# # Generate a random number between 1 and 100
# number = random.randint(1, 100)
#
# # Print the number
# print("The random number is:", number)
#
# # write a code to add numbers 1 to 100
#
# sum = 0
# for i in range(1, 101):
#     sum += i
# print("The sum of all numbers from 1 to 100 is:", sum)
# # making a CHATBOT like chatGPT
# print("Hello! I am elon musk . How can I help you today?")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "hi" or user_input.lower() == "hello":
#         print("musk: Hello there!")
#     elif user_input.lower() == "how are you?" or user_input.lower() == "how are you doing?":
#         print("musk: I'm doing well, thank you for asking!")
#     elif user_input.lower() == "what's your name?" or user_input.lower() == "who are you?":
#         print("myself: My name is Elon musk, and I'm here to help you!")
#     elif user_input.lower() == "bye" or user_input.lower() == "goodbye":
#         print("myself: Goodbye! Have a nice day!")
#         break
#     else:
#         print("myself: Sorry, I didn't get that.")
# # make a function which takes words and tell their length
# words = input("Enter words separated by spaces: ")
# word_list = words.split()
# word_lengths = [len(word) for word in word_list]
#
# print("Lengths of the words:")
# for i, length in enumerate(word_lengths):
#     print(f"Word {i + 1}: {length}")

#
# numbers = [2, 3, 54, 76, 342, 675, 0, -43, -534342,  234, 980, ]
# numbers.sort()
# print(numbers)

#
# number1 = float(input("first number: "))
# number2 = float(input("second number: "))
# result = number1 + number2
# print(result)

#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# o = input("enter the operation you want(a, b, c, division): ")
# a = num1 + num2
# b = num1 - num2
# c = num1 * num2
# division = num1 % num2
# if o : a
# print(a)
# elif  o == b
# print(b)
# elif o== c
# print(c)
# elif o == division
# print(division)
# else print("sorry")
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# print("The sum of", num1, "and", num2, "is", sum)
# print("The difference between", num1, "and", num2, "is", difference)
# print("The product of", num1, "and", num2, "is", product)
# print("The quotient of", num1, "and", num2, "is", quotient)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation!")
    result = None
if result is not None:
    print(f"Result: {result}")

