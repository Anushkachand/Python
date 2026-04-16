# Ques 1. Write a python program to display a user rntered name following by Good Afternoon using input () functiom.
name = input("Enter your name: ")
print(f"Good Afternoon, {name}!")

# Ques 2 . write a program to fill in a letter template given with name and date

letter = '''
       Dear <|Name|>,
       You are selected
       <|date|>
'''
print(letter.replace("<|Name|>", "Harry").replace("<|date|>", "2023-10-10"))


# Q5.  Write a program to fromate the following letter using escape sequance charater.
Letter = " Dear harry , this python course is nice \n Thanks"
print(Letter)


