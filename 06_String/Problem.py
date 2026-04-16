# Q3. Write a program to detect double spaces in a string.

coder = " Python is a high-level, interpreted.  hey "
print(coder.find("  "))  # 


coder = "Apple  is a fruit" 
print(coder.find("  ")) # 6 because ther are space b/w 5 letter.

coder = "Apple is a fruit" 
print(coder.find("  ")) # -1 because there are no double space in the string.

# Q4. Replace double space from Q3 with single space .

print(coder.replace("  ", "")) 

