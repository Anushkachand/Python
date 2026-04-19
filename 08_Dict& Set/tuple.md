# Dictionary
- Dictionary items are **key-value pairs** that are separated by commas and enclosed within curly brackets {}. Dictionary items are stored as key-value pairs, separated by commas and enclosed within curly brackets {}
- 1st element = KEY && 2nd element = value.
 
 Ex:
 ```py
 info = {
    'name':'Karan', 
    'age':19, 
    'eligible':True
    }
print(info)
```

- In Python: dict = HashMap
- Mutable (can change values)
- Values can be any type
- Keys must be unique & immutable (string, int, tuple)


3. Internal Working (IMPORTANT 🔥)
```txt
Uses Hashing
Key → Hash Function → Index → Value
Collision handled internally
```

# Method of Dictionary:



| Method        | Description                          | Example                          |
|---------------|--------------------------------------|----------------------------------|
| get()         | Returns value for a key              | student.get("name")              |
| keys()        | Returns all keys                     | student.keys()                   |
| values()      | Returns all values                   | student.values()                 |
| items()       | Returns key-value pairs              | student.items()                  |
| update()      | Updates dictionary                   | student.update({"age": 21})      |
| pop()         | Removes specified key                | student.pop("age")               |
| popitem()     | Removes last inserted item           | student.popitem()                |
| clear()       | Removes all elements                 | student.clear()                  |
| copy()        | Returns a copy of dictionary         | student.copy()                   |
| setdefault()  | Returns value or sets default        | student.setdefault("grade","A")  |
| fromkeys()    | Creates new dictionary from keys     | dict.fromkeys(["a","b"], 0)      |


- Access → get()
- View → keys(), values(), items()
- Modify → update(), setdefault()
- Delete → pop(), popitem(), clear()
- Copy/Create → copy(), fromkeys()

eg - main.py file


## Set :



