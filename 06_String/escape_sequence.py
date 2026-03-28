# Escape Sequence :
str1 = "I love doing Yoga.\nIt cleanses my mind and my body." # \n is used to print the next line in the string.
print(str1)
# \" = "" 
response = "{\"status\": \"success\", \"code\": 200}"
print(response)

query = "name = \'a " # \' = '
# query = ' name = \'Anu'\
print(query)

# \n = new line
log = "ERROR: Invalid Password\nRetry limit exceeded\nContact admin"
print(log)

# \t = new tab
report = "ID\tName\tScore\n101\tAnushka\t95\n102\tRahul\t88"
print(report)

path = "C:\\Users\\Anushka\\Projects\\app\\config.json"
print(path)

import time
# \r = 
for i in range(3):
    print(f"Processing {i+1}/3", end="\r")
    time.sleep(1)

print("User said \"Login failed\"")
# \t = new tab
print("Product\tPrice\tStock")