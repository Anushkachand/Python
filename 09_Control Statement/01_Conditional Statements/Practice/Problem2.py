# Ques2. Movie Ticket Pricing 
# - Movie Ticket are priced based on age : $12 for adult (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

Age = int(input("Enter the Age: "))
# Age = 2
Day = "Wednesday"
price = 12 if Age >=18 else 8
if Day == "Wednesday":
    price = price -2
print(price)