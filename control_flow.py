# Conditional Statements (if, elif, else):
# Conditional statements are used to execute different blocks of code based on certain conditions. Here's the basic syntax:

# if condition:
# Code block to execute if condition is True
# elif another_condition:
# Code block to execute if another_condition is True
# else:
# Code block to execute if none of the above conditions are True

x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


# Loops (for loop, while loop):
# Loops are used to execute a block of code repeatedly.

# for loop: Used to iterate over a sequence (e.g., list, tuple, string, dictionary, etc.).
# for item in sequence:
# Code block to execute for each item in the sequence

# for indx, item in sequence:
# Code block to execute for each item in the sequence

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, value in enumerate(arr):
    print("Index:", index, "Value:", value)


# while loop: Used to repeatedly execute a block of code as long as a condition is True.
i = 0
while i < 5:
    print(i)
    i += 1


# Control Statements (break, continue, pass):
# break: Terminates the loop immediately, skipping the rest of the code in the loop.
# continue: Skips the rest of the code inside the loop for the current iteration and continues with the next iteration.
# pass: Acts as a placeholder, indicating that no action should be taken. It's used when a statement is syntactically required but you don't want to execute any code.
# Example:

for i in range(10):
    if i == 3:
        continue
    elif i == 7:
        break
    else:
        pass
    print(i)
