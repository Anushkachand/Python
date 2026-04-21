# Conditional Statement :
- it is also know as decision making .

##  conditional statements are classified into the following types: 
1.if
2. if...else
3. elif 
4. nested if

1. If Statement:
- Runs code only if condition is True
- the statement is used to execute one or more staement depending on whether a condition is True or not.

Syntax:
```txt
if condition
    statement
```

ex:
```py
age = 20

if age >= 18:
    print("Adult")
```    

2. if-else Saatement:
- it is execute group of statement when condition is True otherwise it execute another group of statement.

Syntax: 
```txt
if condition
    statement 1
else :
     statement 2
```
ex:
```py
# to know given number is odd or even 
  x = 10
if x % 2 == 0:
    print(x, " is Even no")
else:
    print(x, " is Odd no")
```    

3. elif Statement :
- This structure is used when you need to check multiple conditions and execute only one matching block

```t
if condition1:
    # code block 1
elif condition2:
    # code block 2
elif condition3:
    # code block 3
else:
    # default block
```

## 🔷 Decision Making in Python

| Statement | Syntax | Description | Example |
|----------|--------|------------|---------|
| `if` | if condition: | Executes block if condition is True | if x > 0 |
| `if-else` | if condition: else: | Two-way decision | if x>0 else negative |
| `if-elif-else` | if → elif → else | Multiple conditions | grading system |

---