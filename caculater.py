operation = input("Enter operation (+, -, *, /): ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    result = number1 / number2 if number2 != 0 else "Error! Division by zero."
else:
    result = "Invalid operation!"

print("Result:", result)
