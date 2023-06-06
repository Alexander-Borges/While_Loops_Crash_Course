# How the input() Function Works
# The input() function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.

#message = input("Tell me something and I will repeat it back to you:")
#print(message)

# Letting the User Choose When to Quit
# We can make the parrot.py program run as long as the user wants by putting most of the program inside a while loop. We'll define a quit value and then keep the program running as long as the user has not entered the quit value:
#prompt = "\nTell me something, and I will repeat it back to you."
#prompt += "\nEnter 'quit' to end the program."

#message = ""
#while message != 'quit':
#    message = input(prompt)
#    print(message)

# The above program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes that:
#prompt = "\nTell me something, and I will repeat it back to you."
#prompt += "\nEnter 'quit' to end the program."

#message = ""
#while message != 'quit':
#    message = input(prompt)
    
# if message != 'quit':
    #    print(message)

# Using a Flag
# In the previous example, we had the program perform certain tasks while a given condition was true. But what about more complicated programs in which many different events could cause the program to stop running?
# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active.
# This variable, called a flag, acts as a signal to the program.
prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
        