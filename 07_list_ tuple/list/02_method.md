Method of List : 

list = [10,20,30]

| Method / Function | Purpose                                 | Example                | Output                     |
| ----------------- | --------------------------------------- | ---------------------- | -------------------------- |
| `append()`        | Adds one item at the end of list        | `list.append(50)`       | `[10, 20, 30, 50]`         |
| `extend()`        | Adds multiple items from another list   | `list.extend([40, 50])` | `[10, 20, 30, 40, 50]`     |
| `insert()`        | Inserts item at specific index          | `list.insert(1, 15)`    | `[10, 15, 20, 30]`         |
| `remove()`        | Removes first occurrence of value       | `list.remove(20)`       | `[10, 30, 40]`             |
| `pop()`           | Removes item by index (last by default) | `list.pop()`            | Removes last element       |
| `index()`         | Returns index of value                  | `list.index(30)`        | `2`                        |
| `count()`         | Counts occurrence of item               | `list.count(10)`        | `2`                        |
| `copy()`          | Copies all elemnt into a new list       |                        |                            |
|                   |    and retun it                         | `new_list = lst.copy()` | Same elements copied       |
| `reverse()`       | Reverses the list order                 | `list.reverse()`        | `[30, 20, 10]`             |
| `clear()`         | Removes all elements                    | `list.clear()`          | `[]`                       |
| `sort()`          | Sorts list in ascending order           | `list.sort()`           | `[10, 20, 30]`             |
| `del`             | Deletes element or whole list           | `del list[1]`           | Removes element at index 1 |
| `sum()`           | Returns sum of numeric elements         | `sum(list)`             | `60`                       |
| `len()`           | Returns total number of elements        | `len(list)`             | `3`                        |
| `max()`           | Returns largest element                 | `max(list)`             | `30`                       |
| `min()`           | Returns smallest element                | `min(list)`             | `10`                       |
| `sorted()`        | Returns new sorted list                 | `sorted(list)`          | `[10, 20, 30]`             |
| `list()`          | Converts iterable into list             | `list("abc")`          | `['a', 'b', 'c']`          |


## extend(): This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

ex:
```py
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```


## sort(): This method sorts the list in ascending order.

ex:
```py
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```

## What if you want to print the list in descending order?
- Ans: We must give reverse=True as a parameter in the sort method.
ex:
```py
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```

## Nested Lists:
- Nested Lists allow us to store lists inside another list. These are useful when we want to store structured or table-like data

ex:
```py
# Nested List Example
students = [
    ["Harry", 20],
    ["Sarah", 22],
    ["Bruno", 21]
]

print(students)
```
