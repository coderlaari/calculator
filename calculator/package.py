# Package for Project 1

def calculate_plus(number1, number2):
    answer = number1 + number2
    print(answer)

def calculate_minus(number1, number2):
    answer = number1 - number2
    print(answer)

def calculate_multiplication(number1, number2):
    answer = number1 * number2
    print(answer)

def calculate_division(number1, number2):
    answer = number1 / number2
    print(answer)

def input_numbers():
    input_number1 = input("Give first number, please! ")
    input_number2 = input("Give second number, please! ")
    return int(input_number1), int(input_number2)