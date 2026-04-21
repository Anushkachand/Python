## Ques5. Weather Activity Suggestion
# - Suggest an activity based on the weather (eg: Sunny - Go for a walk , Rainy - Read a book , Snowy - Build a snowman)

# Weather = "Sunny"
Weather = (input("enter the weather:"))

if Weather == "Sunny":
    print("Go for Walk")
elif Weather == "Rainy":
    print("Read a book")
elif Weather == "Snowy":
    print("Build a snowman")
else:
    print("Invalid weather input")