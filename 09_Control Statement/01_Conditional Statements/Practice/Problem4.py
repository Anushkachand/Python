## Ques4. Fruit Ripeness Checker
# - Determine if a fruit is ripe , overripe  or unique bases on its color(eg: Banana : green -Unripe, Yellow - Ripe , Brown - Overripe )


Fruit = "Banana"
Color = (input("Enter the color:"))
if Fruit == "Banana":
    if Color == "Green":
        print("Unripe")
    elif Color == "Yellow":
        print("Ripe") 
    elif Color == "Brown":
        print("Overripe")
    else:
        print("it is not exist")    