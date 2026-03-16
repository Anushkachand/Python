# Math Module
print ("\nMath Module")

import math
from sqlite3 import Time
from xmlrpc.client import DateTime
print("Square Root -", math.sqrt(16))

print("factorial -", math.factorial(6))

# float and celling of 4.7
print("float-", 4.7)
print("cell value of 4.7 -" , math.ceil(4.7))
# Computer 5 raised to the power 3 the math module 
print(" raise to the power -" , math.pow(5,3))


# Random Module
print("\nRandom Module")

import random
print("Random number between 0 and 10 - ", random.randint(1,10)) # random number between 1 and 10
print("Random number between 0 and 1 - ", random.random()) # random number between 0 and 1
list = [10,20,30,40,50,60]
print("Random element from the list - ", random.choice(list)) # random element from the list
#  Shuffle the list [1,2,3,4,5] randomly
i = [1,2,3,4,5]
random.shuffle(i)
print(i)

# Date and Time Module

print("\n DateTime Module")
import datetime
print("Current date and time - ", datetime.datetime.now()) # current date and time
print("Current date -", datetime.date.today()) # current date
today = datetime.date.today()
print("Present year -", today.year) # present year
print("Present Month -", today.month) # present month
print("Present day -", today.day) # present day
