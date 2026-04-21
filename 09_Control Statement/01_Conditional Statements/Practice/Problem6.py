## Ques6. Transportation Mode Selection
# - Choose a mode of transportation based on the distance (eg: <3 km : Walk , 3-15 km: Bike, >15km : Car).

Distance = int(input("Enter the Distance:"))
# Distance = 2
if Distance <3:
    print("Walk")
elif Distance <15 :
    print("Bike")    
elif Distance >15 :
    print("Car")
else:
    print("Enjoy Your life")