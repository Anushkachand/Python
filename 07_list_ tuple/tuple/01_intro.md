# tuple :
tuple is sequence which store a group of element or items. 
- tuple are **immutable**.once we create tuple we cannot modify its element.
- tuples cannot perform operations like append() , eextend (), insert, remove , pop and clear.
- hence we can say that tuple are only store data that cannot modify and retieve that data .

EX:
```py
 tup1 = () # empty tuple , () is parenthesis
```

```py
tup2 = (10,) # single tuple
info = ("Marcus", 20, "MIT")
```



# converting a list into a tuple:
```py
list = [10,20,30,4] # take a list
tup = tuple(list)
print(tup)
```
# Tuple Indexes:
-  Indexes help us access specific items stored inside a tuple. Each item/element in a tuple has its own unique index.

Ex:
```py
 #            [-5]    [-4]     [-3]     [-2]        [-1]
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
```

Accessing tuple items:
1. Positive Indexing:
2. Negative Indexing:
ex:

```py
tuple = (10,2,3,4,29,09)
print(tuple[1]) # postive indexing
print(tuple[-3 :]) # negative indexing 
print(tuple[-5:-3]) 
```

3. Slicing /Range:
```txt
 syntax: tuple_name[start:end:step]
 ```
 ```py 
print(tuple[0:3]) # start from 0 to 2
print(tuple[0:4:2]) # start from 0 to 3 with step 2
print(tuple[::2]) # start from 0 to end with step 2
print(tuple[::-1]) # reverse the tuple
```
4. Check for item:
-  We can check if a given item is present in the tuple. This is done using the in keyword
