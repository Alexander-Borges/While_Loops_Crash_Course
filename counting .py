# Introducing while Loops
# The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the whole loop runs as long as, or while, a certain condition is true.

# The while loop in Action
# You can use a while loop to count up through a series of numbers. 
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Using continue in a Loop
# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.
print('\n')
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding Infinite Loops
# 
# Every while loop needs a way to stop running so it wont't continue to run forever. For example, this counting loop should count from 1 to 5: 
print('\n')
x = 1 
while x <= 5:
    print(x)
    x += 1