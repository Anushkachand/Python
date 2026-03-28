name = "Harry"
print(name[0:3]) # Slicing of String
print (name[-4:-1]) 
print(name[:4]) # is same as print (name[0:4])
print(name[1:]) # is same as print (name[1:5])

nameshort = name[0:6] # string Slicing 
print(nameshort)
char = name[0]
print(char)



Book_name = "ikigai"
Writer = "Hector Garcia"
print(Book_name + "" + Writer)

# Skip Slicing 
website = "Flipkart" 
print(website[0:6:2]) 

story = " Once upon a time there was a youtube named who upload the python Course with notes "

#  string functon
print(len(story))
print( story.endswith("notes"))
print(story.count("a"))
print(story.capitalize()) 
print(story.find("harry")) 
print(story.replace("harry", "code with harry" )) # replace in the string to another string.

stories = "hey i am "
print(stories.strip()) #The strip() method removes any white spaces before and after the string.

#Split & join :

story1 = "hey i am a python developer"
print(story1.split())  # split the string into list of words.
print(",".join(story1)) # join the string with , between each character.



# Format Strings:
name = "Guzman"
age = 18
statement = "My name is {} and my age is {}."
print(statement.format(name, age))

# f-string (Second method of format string)
HelloWorld = " This is my first project is {} and this is first code of {} "
language = "java"
project = " Flipkart clone"

print(f" This is my first project is { project} and this is first code of {language}")

price = 49.8999
txt = f"For only { price: 2f} dollars "
print(txt)

# print (txt.format{})
print(type(f"( 2 *38)"))


''' if any code view  in result then {{comment}} = two curely barcket 
result = comment
'''
print (f" we use string like this : this is my fisrt project is {{project}} and this is my fisrt code is {{ language}} ")

# using expression
price = 50
quantity = 3
print(f"Total cost: {price * quantity} USD")

# formating numbers
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")