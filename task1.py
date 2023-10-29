# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator program
while True:
    # Get user input
    operation = input("Choose an operation (+, -, *, /) or 'q' to quit: ")
    
    # Check if the user wants to quit
    if operation == 'q':
        break

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    # Display the result
    print("Result: ", result)
