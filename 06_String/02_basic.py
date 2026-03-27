name = "Harry"
print(name[0:3]) # Slicing of String
print (name[-4:-1]) 
print(name[:4]) # is same as print (name[0:4])
print(name[1:]) # is same as print (name[1:5])

nameshort = name[0:6] # string Slicing 
print(nameshort)
char = name[0]
print(char)

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