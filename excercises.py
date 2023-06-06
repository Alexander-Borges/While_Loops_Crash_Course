# 1 Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about a car, such "Let me see I can find you a Subaru"
car = input("What kind of rental car would you like? ")

print(f"Let me see if I can find you a {car.title()}.")  

# 2 Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.
group = input("How many in your party?")
group = int(group)

if group >= 8:
    print("\nThere will be a short wait for your table.")
else:
    print("\nYour table is ready.")

# 3 Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not
number = input("Enter a number, and I will tell you if it's a multiple of 10 or not.")
number = int(number)

if number%10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")

# 4 Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.
prompt = "\nWhich toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")

# 5 Movie Tickets: A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over the age of 12, the ticket is $15. Write a loop in which you ask the user's age, and then tell them the cost of their ticket.
while True:
    age = input("Enter your age (or 'quit' to exit): ")
    if age.lower() == 'quit':
        break

    age = int(age)
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"The cost of your ticket is ${ticket_price}.")