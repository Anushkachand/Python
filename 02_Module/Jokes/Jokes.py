# Import and print random joke
from random import choice

import pyjokes
print(pyjokes.get_joke())  # print random jokes  [TCS NQT (2022, 2023) , Wipro (2022)]

jokes = pyjokes.get_jokes()
for j in jokes[:3]: # print 3 jokes [ Infosys (2023)]
    print(j)

#  Using Category
jokes = pyjokes.get_jokes(category = 'neutral') # [ Deloitte (2024), Deloitte (2024)]
print(jokes)   # print jokes of category netural 

#  Using Language
print("English:", pyjokes.get_joke(language='en')) 
print("German:", pyjokes.get_joke(language='de'))

#  Store Joles in list
Jokes = pyjokes.get_jokes()
print(Jokes[1]) # print 2 jokes from list
print(Jokes[2]) # print 3 jokes from list

# Random Joke Function
def random_jokes():         # [ Accenture (2023), Deloitte( 2024)]
    return pyjokes.get_jokes() 

# User Input Based Joke ⭐
lang = input ("Enter the language (en/de /es)")  # [ TCS interview , 2023] , [ Google(2024), Infosys(2024)]
# lang = input("Enter language: ") upper code and this code both are same
print(pyjokes.get_joke(language=lang))


choice = int(input("Enter choice: "))
if choice == 1:    # [ Deloitte (2024 Interview)], [ == → comparison operator (equal check karta hai) ]
    print(pyjokes.get_joke()) 

# 🔹 Custom Joke Picker
import random
print(random.choice(jokes))   # you can also use random choice to pick a random joke from the list of jokes [Deloitte (2024)]
