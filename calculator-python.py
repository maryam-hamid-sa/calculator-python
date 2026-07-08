# Calculator using Python
num1 = float(input("enter first number: "))
operator = input("Choose operator (+, -, *, /): ")
num2 = float(input("enter second number: "))
if operator == "+":
    print("result:", num1 + num2)
elif operator == "-":
    print("result:", num1 - num2)
elif operator == "*":
    print("result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")