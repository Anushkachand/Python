## Method of Tuple:

# Python Tuple Reference

Tuples are immutable sequences, typically used to store collections of heterogeneous data. Below are the built-in functions used to manipulate and query tuples.

## Built-in Utility Functions

| Function   | Description                                            | Example         |
| :---       | :---                                                   | :-----          |
| `len()`    | Returns the total number of items in the tuple.        | `len(my_tuple)` |
| `max()`    | Returns the item with the highest value.               | `max(my_tuple)` |
| `min()`    | Returns the item with the lowest value.                | `min(my_tuple)` |
| `sum()`    | Returns the sum of all numerical elements.             | `sum(my_tuple)` |
| `sorted()` | Returns a **new sorted list** of the tuple's elements. | `sorted(my_tuple)` |
| `any()`    | Returns `True` if any element in the tuple is true.    | `any(my_tuple)` |
| `all()`    | Returns `True` if all elements in the tuple are true.  | `all(my_tuple)` |
  
---

## Manipulating Tuples:

## Summary: Tuple Operations vs. Results

Since tuples are immutable, "modifying" them always results in the creation of a **new tuple** object in memory.

| Goal                  | Technique                         | Resulting Type |
| :---                  | :---                              | :---           |
| **Change an item**    | `list()` → `index` → `tuple()`    | New Tuple      |
| **Add an item**       | Concatenation (`+`)               | New Tuple      |
| **Remove an item**    | Slicing or List conversion        | New Tuple      |
| **Combine tuples**    | Concatenation (`+`)               | New Tuple      |
| **Duplicate content** | Multiplication (`*`)              | New Tuple     |

---

### Why use a New Tuple instead of a List?
1. **Memory Efficiency:** Tuples are fixed-size and generally use less memory than lists.
2. **Thread Safety:** Being immutable makes them safer to use in multi-threaded environments.
3. **Data Integrity:** Ensures that constants or configurations remain unchanged throughout the program execution.

# Unpack Tuples?

-Tuple unpacking allows us to extract values from a tuple and assign them to variables in a single line. Unpacking is the process of assigning the tuple items as values to variables.

```
info = ("Marcus", 20, "MIT")
(name, age, university) = info
print("Name:", name)
print("Age:", age)
print("Studies at:", university)
```


# Rule of *
*variable gathers all remaining items
It always becomes a list
You can use only ONE * variable in unpacking.

```py
fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, bird, fish) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)
```