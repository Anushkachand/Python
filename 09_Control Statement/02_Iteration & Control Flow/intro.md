## Iteration
- Loops are used in programming to execute a block of code repeatedly until a specified condition becomes false.(jab tak condition true hai, tab tak code chalta rahe)
ex:
```
for i in range(1, 6):
    print(i)
```    

# Types of Loops in Python:
1.For Loop
2.While Loop

---
1. For Loop
-  a control flow statement used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in that sequence

Syntax:
```
for item in sequence:
    # block of code to execute
```

ex:
```py
n = 7
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

print(is_prime)
```


# 2. While Loop
- In while loop the condition is checked firstand then it evaluate to true , the body of loop is exectute otherwise not.

### Syntx:
```
while condition:
    # code block
 ```

 eg:
 ```py
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
 ```

 ```
 for i in range(1, 5):
    print("*" * i)
``` 

## Nested Loops:
We can use loops inside other loops, such types of loops are called nested loops.

Example: nesting for loop in while loop

```py
while (i <= 3):
    for k in range(1, 4):
        print(i, "*", k, "=", (i * k))
    i = i + 1
    print()
``` 

# Control Statetment
1 , pass → do nothing
2. continue → skip current iteration 
3. break → exit loop 

1. Pass:
- 


| Statement  | Use            |
| ---------- | -------------- |
| `pass`     | Do nothing     |
| `continue` | Skip iteration |
| `break`    | Exit loop      |
