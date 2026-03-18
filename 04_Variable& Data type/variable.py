# Variable is container hold the data.
a = 1   # type int
print(a)
b = "harry "   # type str
print(b)
a1 = 9
print(a+a1)
print("type of a is", type(a))   # type of variable
print("type of b is", type(b))  # type of variable 
# Multiple assignament 
a, b, c = 1, 2, 3
# Same value assign to multiple variable
x = y = z = 100

#  Type Checking
x = 10

a = 10 
b = 10
print(a is b) # type checking for small integers ( imp question)

# Variable scope
x = 10
def func():
    # print(x)  # this will give error because x is not define in the local scope of func
    x = 20 

func()

#  Local Variable :

Book = "Review of The Art be Alone " 

def show_book_details():
    # local variables
    writer_name = "Renuka Gavrani"
    publish_year = 2000
    
    print(f"Book: {Book}") # Global variable can be accessed inside the function
    print(f"Writer: {writer_name}") 
    print(f"Publish Year: {publish_year}") 

show_book_details()

# Attempting to access the local 'director' variable here would cause a NameError
# print(director) 

# Global Varialbe:
# global variable - can be accessed anywhere in the code, including inside functions or outside functions.
car_brand = "Tata" 

def print_car_info():
    # another local variable
    model = "Nexon" 
    
    print(f"The brand inside the function is: {car_brand}") # Accessing the global variable
    print(f"The model inside the function is: {model}")

print_car_info()

print(f"The brand outside the function is: {car_brand}") # Accessing the global variable
# Attempting to access the local 'model' variable here would cause a NameError
