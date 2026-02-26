def calculator(choice, a, b):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a / b
    else:
        return "Invalid choice"
    
print("----------Calculator----------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")
print("-------------------------------")

choice = int(input("Enter choice (1/2/3/4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = calculator(choice, a, b)
print("-------------------------")
print("Result: ", result)
print("-------------------------")