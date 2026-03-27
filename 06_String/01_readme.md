# String 

- String is a data type in python.
- string is sequnce of charater enclose in quotes("").
- Immutable 

## 3 way to represent :
```python
a = 'Anu'    # Single quotes String
a = "Andersen Fair Tales " # Double quote String 
a  = '" Hand Christian"' # Triple quotes String 
```

# Operation on Strings

##  String Slicing 
- The index in string start from 0 to (lenght-1) in Python. 
Syntax:
```
string[start : end : step]
```
### reverse a string : 

```python 
text = "Python"
print(text[::-1]) 
```

- Slicing with skip value 
```python
website = "Flipkart" 
print(website[0:6:2]) # 0 is starting index, 6 is ending index and 2 is skip value.
```

------------------------------------------------

# Function of String:

1. Length of a String: The function written lenght of string.
Ex:
```
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```

2. Loop in String:
```python
# company = " Flipkart "
company = [ "Flipkart", "Amazon", "Mntra", "Sony" ]
for i in company:
    print(i)
```

### Ques.1. Difference between upper(), lower(), capitalize(), title()?
Ans:
- upper() → ALL characters uppercase
- lower() → all lowercase
- capitalize() → only first letter uppercase
- title() → first letter of each word uppercase

### Q2. Difference between find() and index()? [imp]
Ans: 
find() → returns -1 if not found
index() → raises error if not found

Example:
``` python
            text = "Python"
            print(text.find("z"))   # -1
            print(text.index("z"))  # ValueError ❌
````

-----------------------

## Ques3. Difference between isalnum() and isalpha()

Answer:
- isalnum() → letters + numbers
- isalpha() → only letters

💡 Example:
```python
    print("abc123".isalnum())  # True
    print("abc123".isalpha())  # False
```

