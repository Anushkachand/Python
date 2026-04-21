
## Ques3. Grade Calculation
# - Assign a letter garde based on a student score: A(90-100), B(80-89), C(70-79), D(below 60) 

score = int(input("enter the number:"))
if score >100:
   print("Please verify your grade again")
   exit()
   
elif score <100:
   grade = "A"
elif score <80:
   grade = "B" 
elif score <70:
   grade = "C"
else:
   grade = "F"   
print("Grade:", grade)        