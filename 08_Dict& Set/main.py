student = {
    "name": "Anushka",
    "age": 20,
    "course": "BTech"
}
print(student)

print("\n Method of Dictionary")
print(student.get("name"))  # get method is used to access the value of a key in a dictionary.    

# display only keys of the dictionsary 
print('Key in dict =', student.keys())
print('Values in dict =', student.values())# display only values of the dictionary
print('Items in dict =', student.items()) #  display both keys and values of the sictionary 

# Update the value of a key in the dictonary using the update() method. The update() method is used to add or update key-value pairs in a dictionary.
student.update({"age": 21})
student.update({"city": "Lucknow"})
print('Updated dict =', student)


# setdefault() → Add only if key not present
student.setdefault("age",28) # it will not update the value of age because age key is already present in the dictionary
student.setdefault("country","India") # it will add the key country with value India because country key is not present in the dictionary (Add only if key not present)
print('Updated dict =', student)

student.pop("age") # Removes specified key
print('Dict after popping "age" =', student)

student.popitem() # Remove last inserted item
print('Dict after popping last item =', student)

# student.clear() # removes all items
# print(student)

info = {' Country name':'Russia', 'GDP' : 5, 'eligible':True, }
newDictionary = info.copy()
print(newDictionary)

