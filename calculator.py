print("========================================")
print("-------Welcome to the Calculator!-------")
print("========================================")

while True: 


 number1 = float(input("Enter the first number: "))
 number2 = float(input("Enter the second number: "))

 chose_sympol = input("Enter the symbol (+, -, *, /): ")

 if chose_sympol == "+":
    result = number1 + number2
    print(f"ANSWER IS: {result}")
 elif chose_sympol == "-":
    result = number1 - number2
    print(f"ANSWER IS: {result}")
 elif chose_sympol == "*":
    result = number1 * number2
    print(f"ANSWER IS: {result}")
 elif chose_sympol == "/":
    result = number1 / number2
    print(f"ANSWER IS: {result}")

 else:
    print("Invalid symbol. Please enter a valid symbol (+, -, *, /).")

 again = input("Type 'stop' to exit, or press Enter to continue: ")

 if again.lower() == "stop":
    print("Thank you for using the calculator. Goodbye!")
    break
   