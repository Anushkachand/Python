# Quue1. Age Group Categorization
# - Classify a person's age group: Child(<13), teenager(13-16), Adult(20-59),Senior(60+).

# Age = 47
Age = int(input("enter the number:"))
if Age< 13:
    print("Child")
elif Age<20:
    print("teenager")
elif Age <60:
    print("Adult")
else:
    print("Senior")        

