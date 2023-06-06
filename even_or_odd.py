# The Modulo Operator
# A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder:

# The modulo operator doesn't tell you how many times one number fits into another, it just tells you what the remainder is. 
# >>>4 % 3
# 1
# >>>5 % 3
# 2
# >>>6 % 3 
# 0
# >>>7 % 3
# 1  

# You can use the modulo operator to determine if a number is even or odd:
number = input("Enter a number, and I'll tell you if it's even or odd.")
number = int(number)

if number %2 == 0:
    print(f"\nThe number {number} is odd.")
else:
    print(f"\nThe number {number} is odd.")
    
