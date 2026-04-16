
#  Modules 

### 1.  Module

A ** Module** is a file with a `.py` extension that contains
functions, variables, or classes which can be reused in another Python
program.

It helps in: - Code reuse - Better program organization - Easier
maintenance

✅ Advantages

- Code Reusability ♻️
- Better Organization 📂
- Easy Maintenance 🔧
- Reduces Code Duplication

### Common Built‑in Modules

-   `math`
-   `random`
-   `datetime`
-   `json`
-   `csv`
-   `sqlite3`
-   `statistics`
-   `tkinter`
-   `turtle`

### Example

``` python
  import math
   print(math.sqrt(36))
```

**Output**

    6.0

------------------------------------------------------------------------

## 2. Creating Your Own Module

You can create your own module by saving functions in a `.py` file.

### module.py

``` python
    def add(a,b):
    return a+b

def sub(a,b):
    return a-b
```

### calc.py

``` python
import module
print(module.add(5, 3))
```

------------------------------------------------------------------------

## 3. Using Alias

- You can give a short name (**alias**) to a module using `as`.

### Example

``` python
import math as m
print(m.sqrt(36))
```

------------------------------------------------------------------------

## 4. Import Specific Functions

Instead of importing the whole module, you can import only the required
functions.

### Example

``` python
from module import add, sub
um1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(add(10, 5))
```

⚠️ If you try to use a function that is **not imported**, Python will
raise a **NameError**.

------------------------------------------------------------------------

## 5. Import Everything (\*)

You can import all functions from a module using `*`.

### Example

``` python
from module import *
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(add(10, 5))
print(sub(10, 5))
```

⚠️ This method is generally **not recommended in large programs**
because it can create confusion about where functions come from.

------------------------------------------------------------------------

## 6. `dir()` Function

The `dir()` function shows all functions and variables available inside
a module.

### Example

``` python
from operator import mod
import math

lst1 = dir(math)
print(lst1)
```
This will display all available functions such as:

-   `sin()`
-   `cos()`
-   `sqrt()`
-   `log()`
-   and many more.

------------------------------------------------------------------------

## Summary

Python modules help developers: - Reuse code - Organize programs
better - Access powerful built‑in functionality

Using modules makes Python programs **cleaner, modular, and easier to
maintain**.

