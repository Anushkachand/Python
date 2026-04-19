a = (1, 2, 3)
print(a)
print(type(a))
list = [10,20,30,4] # take a list
tup = tuple(list) # convert list into tuple
print(tup)

# indexing:
tuple = (10,20,30,40,90,67,45)
print(tuple[0]) # postive indexing
print(tuple[-1]) # negative indexing
print(tuple[-4:-1]) # negative indexing range
print(tuple[-4:])

# Slicing /Range:
print( "  \n Range of tuple")
print(tuple[0:3]) # start from 0 to 2
print(tuple[0:6:2]) # start from 0 to 5 with step 2
print(tuple[::2]) # start from 0 to end with step 2
print(tuple[::-1]) # reverse the tuple

# method of Tuple :
print("\n Mmethod of tuple")
info = ("Anushka" , 30 , "Lucknow")
# print(info.append("India")) # append is not allowd in tuple 
print(info.count("Project")) # count  the number of items in tuple
print(info.index(30)) # return the index of first occurance of the specified value 
print(info.__len__()) # return the number of items in the tuple
# print(sorted(info)) # sorted is not allowed in tuple


print("\nConcation of Tuple")
countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (10,20,30,40,90,67,45)
print(sorted(tuple1)) # sorted is not allowed in tuple but we can sort the tuple by converting it into list

print("\n Unpacking of Tuple")
fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)