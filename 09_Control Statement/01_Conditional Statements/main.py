# if statement 
print(" if statement\n")
x = 5
if x>0:
    print(x, "is a postive number")

# if else statement

print("\n if else statement\n")
x = int(input("Enter a number:"))
if x % 2 == 0:
    print(x, " is Even no")
else:
    print(x, " is Odd no")

# using and operator in if else statement

x = int(input("Enter a number:"))
if x>1 and x<10:
    print(x , "is between 1 and 10")
else:
    print("x is less than 10")


# if else if statement 

print("\n if else if statement\n")
temperature = 30

if temperature > 35:
    print("Very Hot")
elif temperature > 25:
    print("Warm")
else:
    print("Cool")

# Nested if Statement
print("\n Nested if Statement\n")
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")