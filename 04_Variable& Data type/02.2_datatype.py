# pyq question all tech compaines 
x = [1, 2, 3]
y = x
x = x + [4]   # x = x + [4] creates a new list
print(y)      # y still points to old list

x = [1, 2, 3]
y = x
x.append(4) # append() modifies same object
print(y)

int1 = -2345698
int2 = 0
int3 = 100548

print(type(int1))
print(type(int2))
print(type(int3))

# Example of a mutable data type (list)
fruits = ["apple", "banana", "cherry"]
print(id(fruits))  # Memory address before modification

fruits.append("mango")  # Adding a new item
print(fruits)
print(id(fruits))  # Same memory address → same object

# Example of an immutable data type (string)
name = "Sita"
print(id(name))  # Memory address before modification

name = name + " Ram"  
print(name)
print(id(name))  # Different memory address → new object created

# typecasting
a = 5       # int
b = 2.5     # float
c = a + b
print(type(c))  

# int to float
print(float(5))   

# float to int
print(int(5.9))   

# string to int
print(int("10"))  

# list to set
print(set([1,2,2,8]))  

print(str(10) + str(20))