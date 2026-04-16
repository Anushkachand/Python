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

