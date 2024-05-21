def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: division by zero is not possible.")
                continue
        else:
            print("Not correct operator.")
            continue

        print(f"Result: {result}")

        continue_calculation = input("Do you like to continue? (yes/y for continue): ").lower()

        if continue_calculation != "yes" and continue_calculation != "y":
            print("Work completed.")
            break
calculator()