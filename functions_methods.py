"""
In Python, you declare a function using the def keyword followed 
by the function name and parentheses containing any parameters 
the function takes. Here's the basic syntax:
"""


def function_name(parameter1, parameter2):
    x = parameter2
    y = parameter1
    # Function body
    # This can be one or more statements
    # Optionally, you can return a value using the return statement
    return value


def add_numbers(a, b):
    sum = a + b
    return sum


# You can call this function by using its name and passing arguments:
result = add_numbers(3, 5)
print(result)  # Output will be 8


# Functions in Python can have default parameter values and can return multiple values as tuples. Here's an example:
def greet(name="Guest"):
    return "Hello, " + name


print(greet())  # Output: Hello, Guest
print(greet("Alice"))  # Output: Hello, Alice


def add_and_subtract(a, b):
    add = a + b
    subtract = a - b
    return add, subtract


result_add, result_subtract = add_and_subtract(8, 3)
print("Addition:", result_add)  # Output: Addition: 11
print("Subtraction:", result_subtract)  # Output: Subtraction: 5

