def calculator():
    """
    A Simple calculator function that performs basic arithmetic operations
    """
    print("Welcome to the calculator!")
    
    # Get the first two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Get the operation from the user
    operation = input("Enter the operation (+, -, *, /): ")

    # perfrom the calculation based on the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation. Please try again.")
        return
    
    # Print the result
    print(f"{num1} {operation} {num2} = {result}")
    
    
# Call the calculator function
calculator()