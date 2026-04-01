
# Tricky Questions Asked

1. Difference:
   - list[2] → single element  
   - list[2:3] → list  

2. Output-based:
   animals[-1:-5] → ❌ Empty (wrong direction)

3. Reverse list:
   animals[::-1]

## Q4: Difference between append() and extend()?

Answer: append() → adds whole object  
- extend() → adds elements of object  

Example:

```py
a = [1,2]
a.append([3,4]) → [1,2,[3,4]]
a.extend([3,4]) → [1,2,3,4]
```

### 🔸 PYQ 4 (Capgemini)
a = [1,2]
print(a + [3,4])

✅ Answer: [1,2,3,4]  
👉 New list created

---