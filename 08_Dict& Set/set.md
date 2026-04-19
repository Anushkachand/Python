##  What is a Set?

* Unordered collection of **unique elements**
* No duplicates allowed

```python id="2v8y6s"
s = {1, 2, 3}
```

---

## Key Features

*  No duplicate values
*  Unordered
*  Mutable (can add/remove)
*  No indexing

---

# Add / Remove Items

```python 
s.add(4)        # Add item
s.remove(2)     # Remove (error if not found)
s.discard(5)    # No error if not found
s.pop()         # Remove random item
```

---

## 🔹 Join Sets

```py
a = {1,2,3}
b = {3,4,5}

print(a.union(b))        # {1,2,3,4,5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1,2}
```

---

## 🔹 Set Methods 🔑

| Method         | Description        |
| -------------- | ------------------ |
| add()          | Add element        |
| remove()       | Remove element     |
| discard()      | Remove (no error)  |
| pop()          | Remove random item |
| clear()        | Remove all items   |
| union()        | Combine sets       |
| intersection() | Common elements    |
| difference()   | Unique elements    |
| issubset()     | Check subset       |
| issuperset()   | Check superset     |

--- 

## 🔹 Use Cases 💡

* Remove duplicates
* Membership testing (`in`)
* Mathematical set operations


