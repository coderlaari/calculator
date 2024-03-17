import package as calculate

calculate_what = input("What you want to calculate? (plus, minus, division or multiplication) ")

if calculate_what == "plus":
    what_to_calculate_plus1, what_to_calculate_plus2 = calculate.input_numbers()
    calculate.calculate_plus(what_to_calculate_plus1, what_to_calculate_plus2)

if calculate_what == "minus":
    what_to_calculate_minus1,what_to_calculate_minus2 = calculate.input_numbers()
    calculate.calculate_minus(what_to_calculate_minus1, what_to_calculate_minus2)

if calculate_what == "multiplication":
    what_to_calculate_multiplication1, what_to_calculate_multiplication2 = calculate.input_numbers()
    calculate.calculate_multiplication(what_to_calculate_multiplication1, what_to_calculate_multiplication2)

if calculate_what == "division":
    what_to_calculate_division1, what_to_calculate_division2 = calculate.input_numbers()
    calculate.calculate_division(what_to_calculate_division1, what_to_calculate_division2)