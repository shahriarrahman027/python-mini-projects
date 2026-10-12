# Simple Calculator Program

# A. Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# B. Perform basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check whether the second number is zero before division
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# C. Display the results with clear labels
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
