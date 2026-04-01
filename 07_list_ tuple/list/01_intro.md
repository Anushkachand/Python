# Lists

- Lists are **ordered collections**.
- They store **multiple items** in a single variable.
- List items are separated by **commas and enclosed** within square brackets [].
- Lists are **mutable** (can change)
- Indexing is **O(1)** (fast access)
- Slicing creates a **new list (O(n))**

Example :

```py
lst1 = [1, 2, 2, 3, 5, 4, 6]
print(lst1)
```

## Python List Indexing & Slicing

## 1.List Index

- Each element has a **unique index**.
- Indexing starts from **0**.

Example:

```py
#          [-5]   [-4]     [-3]     [-2]      [-1]   # Negative Indexing (Starts from **-1 (right to left)**)
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]  # Postive Indexing ( Start from **0 (left to right)**)

```

Example:

```py
Marks = [10,20,30,4,60,]
print(Marks[2]) → Blue   # postive index
print(colors[-1])  # negative index
```

## Membership Check (`in` keyword)

- Checks if element exists in list

Example:

```py
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
```

- Time Complexity: O(n)

---

## List Slicing

Syntax:

```

List[start : end : step]
```

- `start` → inclusive  
- `end` → exclusive  
- `step` → jump index  

## Range Slicing

Example:

```py
cars = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW']
Car[3:7] 
cars[-7:-2] 
print(Cars[1:8:3]) # jump indexing
```

---

## ⭐ Real-World Use Cases

- Data filtering 📊
- Log analysis 📜
- API response slicing 🌐
- Pagination systems 📄

---

👉 Imp point:

- Indexing = O(1)
- Slicing = O(n)
- Negative indexing = shortcut for last elements

- Use slicing smartly instead of loops to reduce code complexity.

---

## Add List Items

- There are three methods to add items to a list: append(), insert(), and extend()

## 📘 Python List Methods (append, insert, extend) – Placement Notes

---

## 1. append()

- Adds **single element** at the **end** of list
- Only **one element** at a time
Example:

```py
colors = ["violet", "indigo", "blue"]
colors.append("green")
```

---

## 2. insert(index, element)

- Inserts element at a **specific index**
- used when **position matters**

---

## 3. extend(iterable) 🔗

- Adds **multiple elements** from another collection
- **iterates and adds elements individually**

## 🔹 4. Concatenation (+) ➕

- Combines two lists and returns **new list**
ex:
```py
colors = ["violet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```

👉 Always mention:

- Time Complexity:
  - append() → O(1)
  - insert() → O(n)
  - extend() → O(n)

👉 Use extend() for performance instead of loop append

👉 Remember:
append = add 1  
extend = add many  
insert = add at position  

---

## Creating List Using Range Function()

- We can use  range function to generate a **sequence of integer** which can be stored in a list.

- syntax:

```text
range(start , stop , stepsize )
```

### Range using loop

Q. What is a range object in Python?

- we can say **range object is iterable** .that generates numbers in a sequence one by one. It is commonly used in loops and functions that require successive values

Q. Why range use?

- range() is used to generate a sequence of numbers, mainly for loping a specific number of times.

Q. Why **range memory is efficent** ?
Ans:Because it generates values one by one instead of storing all numbers in a list at once .

Example:

```py
list1 = list(range(10))
for i in list1: # display elements by element
    print(i , "," , end = " ") # end = " " is used to print in the same line  
print() # throw to nxt line 
print(list1)   # display whole list at once

# Create a list with integer from 5 to 9
list2 = list(range(5,9))
for i in list2: 
    print(i , "," , end = " ") # end = " " is used to print in the same line  
print() 
print(list2)   
# create list with odd number from 1 to 0 
list3 = list(range(1,10,2)) # crate list with odd no from 1 to 9
for i in list3: 
    print(i , "," , end = " ") # end = " " is used to print in the same line  
print() # throw to nxt line 
print(list3)   
```

# using loop:

```py
list = [10,20,30,40,56]
print("using loop")
i = 0 
while i < len(list): # repeat until i is less than length of list4
    print(list[i]) 
    i = i +1 
    print("for loop")
for i in list:
    print(i)
```

# Change List Items
Replace a single item by using its index

```py
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie" # change element at index 2 to Millie
print(names)
```

