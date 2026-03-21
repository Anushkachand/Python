# Data type:
Data type specific the type of value a variable hold. 
This is required in programming to do various operations whithout causing an error.

ex:
```python
      a = 1
      print(type(a))
```
#  1. Numeric Data
- **int** → Whole numbers → `3, -8, 0`
- **float** → Decimal numbers → `7.349, -9.0`
- **complex** → `a + bj` → `6 + 2j`

---

# 2. Text Data
- **str** → Sequence of characters  
  Examples:
  ```python
  "Hello World!!!"
  "Python Programming"

#  3. Boolean Data
- Values: True or False

# 4. Sequence Data:  list, tuple, range

## a. List (Mutable)
- Ordered collection
- Can be modified

ex:
```python 
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```

## b. Tuple (Immutable)
- Ordered collection
- Cannot be modified

```python
tuple = (("Apple , "Mango") , "banana", "cherry")
print(tuple)
```

# range:
-  Returns a sequence of numbers as specified by the user. If not specified by the user, it starts from 0 by default and increments by 1

```python
sequence1 = range(4, 14, 2)
for i in sequence1:
    print(i)
```

#  5. Dictionary (Mapped Data)
- Key-value pairs

```python
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
```

# Set:
- A set is unorder collection of element in which no element is repeated . 
- the element seoreate by (,) and contain within a curly bracket({}).

EX:
```python
set1 = {4,-5,8,9,1}
print(ste1)
```

# Memoey View : memory view() function return a memory view object from specifed object.

Example:
```python
str1 = bytes(" home" "utf-8")
memoryviewstr = memoryview(str)
print(list(memoryviewstr[0]))

# Mutable vs Immutable Data Type

## Mutable means changeable.
- If a data type is mutable, it means you can add, remove, or modify its elements without creating a new object in memory. When you change a mutable object, its memory address (ID) stays the same.

## Common mutable data types:
- list
- dict
- set

# Immutable Data Types :
Immutable means unchangeable. If a data type is immutable, it means its value cannot be changed once created. If you try to modify it, Python will create a new object instead of changing the existing one. As a result, its memory address (ID) changes.

## Common immutable data type:
- int
- float
- complex
- str
- tuple
- bool
- bytes
------------------------------------------------------------------------------
- **Mutable** → Can change value (same memory )
- **Immutable** → Cannot change value (new object created )

# Key Differemce between :

+--------------+-------------------+----------------------+
| Feature      | Mutable 🔵        | Immutable 🔴         |
+--------------+-------------------+----------------------+
| Change Value | Yes               | No                   |
| Memory ID    | Same              | Changes              |
| Performance  | Faster updates    | Safer, more secure   |
| Examples     | list, dict, set   | int, str, tuple      |
+--------------+-------------------+----------------------+
