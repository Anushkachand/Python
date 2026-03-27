# Variable : 
- Variables are containers that store information that can be manipulated and referenced later by the programmer within the code.
 - Variables are containers for storing data values.
Example:
```
name = "Anushka"   # type str
age = 20            # type int
passed = True       # type bool
````

# ✅ Rules for define variable name:

- Variable names can only contain alphanumeric characters and underscores (A-Z, 0-9, and _).
- No special symbols ($, @, #, etc.)
- Variable names must start with a **letter** or the underscore character.
- Variables are case sensitive.
- Variable names ❌ cannot start with a number.

Example:
```
       color = "yellow"     # valid
       _color = "blue"      # valid
       Color = "green"      # valid
       
       5color = "red"       # ❌ invalid
       $color = "orange"    # ❌ invalid
```
# ✨ Readability Patterns (Naming Styles)

- Choose a consistent style based on context
```
    NameOfCity = "Mumbai"      # PascalCase (used in classes)
    nameOfCity = "Berlin"      # camelCase (common in JS, sometimes Python)
    name_of_city = "Moscow"    # snake_case (Python standard ✅)
```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Scope of a Variable:

- The scope of the variable is the area within which the variable has been created. Based on this, a variable can have either a local or a global scope.
  
# Local Variable:
- A local variable is created within a function and can only be used inside that function. Such a variable has a local scope.
- Defined inside a function
- Accessible only within that function
- Helps in encapsulation & memory efficiency

Example:
```
    def fun():
        x = 10   # local variable
        print(x)
    
    fun()
```
# 🔹 Global Scope

- Defined outside all functions
- Accessible throughout the program
- A global variable is created in the main body of the code and can be used anywhere within the code. Such a variable has a global scope.
Example:
```
      x = 10   # global variable
      
      def fun():
          print(x)
      
      fun()
```
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🎯 Key Differences of Gobal and Local Scope:
| Feature   | Local Variable        | Global Variable        |
|-----------|---------------------|------------------------|
| Defined   | Inside a function    | Outside any function   |
| Scope     | Only inside function | Entire program         |
| Lifetime  | Temporary            | Till program ends      |
| Access    | Limited              | Accessible everywhere  |

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Imp and PYQ Questions:

- Tricky & Placement-Level Questions

Concept: Memory optimization / interning
```
     a = 10
     b = 10
     print(a is b)

```

 # Ques.  Variable scope

 ```
   x = 10
   def func():
       # print(x)  # this will give error because x is not define in the local scope of func
       x = 20 
   func()
```
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🧠 LEGB Rule in Python

LEGB stands for:

👉 L → Local
👉 E → Enclosing
👉 G → Global
👉 B → Built-in

📌 It defines the order in which Python searches for a variable.


# LEGB:

| Scope      | Where Defined      | Keyword     | Key Points                         |
|------------|-------------------|-------------|------------------------------------|
| Local      | Inside function   | ❌ No        | First priority; temporary          |
| Enclosing  | Outer function    | ✅ nonlocal  | Used in nested functions           |
| Global     | Outside function  | ✅ global    | Accessible everywhere              |
| Built-in   | Python predefined | ❌ No        | Default functions (print(), len()) |
------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

a