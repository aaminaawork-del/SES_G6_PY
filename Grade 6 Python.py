# Grade 6 Python Program: Variables, Data Types, Input/Output, and Operators
# Reference: Introduction to Python

# 1. Variables and Data Types
student_name = "Alex"  # String data type (text)
student_age = 13  # Integer data type (whole number)
item_price = 45.5  # Float data type (decimal number)
is_enrolled = True  # Boolean data type (True/False)

# 2. Displaying initial information using print()
print("--- Student Profile ---")
print("Name:", student_name)
print("Age:", student_age)
print("Item Price:", item_price)
print("Enrollment Status:", is_enrolled)

# 3. Taking User Input
num1 = int(input("\nEnter first whole number: "))  
num2 = int(input("Enter second whole number: "))  

# 4. Arithmetic Operators (+, -, *, /, %, **)
print("\n--- Arithmetic Operations ---")
print("Addition (+):", num1 + num2)  
print("Subtraction (-):", num1 - num2)  
print("Multiplication (*):", num1 * num2)  
print("Division (/):", num1 / num2)  
print("Modulus (% - Remainder):", num1 % num2)  
print("Exponentiation (** - Power):", num1**num2)  

# 5. Comparison (Relational) Operators (>, <, ==, !=, >=, <=)
print("\n--- Comparison Operations ---")
print("Is num1 greater than num2?", num1 > num2)  
print("Are both numbers equal?", num1 == num2)  
print("Are the numbers not equal?", num1 != num2)  

# 6. Logical Operators (and, or, not)
cond1 = num1 > 5
cond2 = num2 > 5
print("\n--- Logical Operations ---")
print("Both numbers > 5 (and):", cond1 and cond2)  
print("At least one number > 5 (or):", cond1 or cond2)  
print("Inverse of condition 1 (not):", not cond1)  
