list1 = list(range(10))
for i in list1: # display elements by element
    print(i , "," , end = " ") # end = " " is used to print in the same line  
print() # throw to nxt line 
print(list1)   # display whole list at once
  
# create list with odd number from 1 to 0 
list3 = list(range(1,10,2)) # crate list with odd no from 1 to 9
for i in list3: 
    print(i , "," , end = " ") # end = " " is used to print in the same line  
print() # throw to nxt line 
print(list3)   

list = [10,20,30,40,56]
print("using loop")
i = 0 
while i < len(list): # repeat until i is less than length of list4
    print(list[i]) 
    i = i +1 
    print("for loop")
for i in list:
    print(i)


#  Method of list :
number = [10,20,30,40,60]
n = len(number) # lenght of list
print("lenght of list is : ", n)\

number.append(70) # add element at the end of list
print("list after appending 70 : ", number)

num = number.copy() # copy list to another list
print("copy of list is : ", num)

number.insert(2,25) # insert element 25 at index 2
print(number)

number.sort() # sort the list in ascending order 
print(number)

number.reverse() # reverse the list 
print(number)

number.remove(30) 
print(number)

number.pop(3) # remove element at index 3
print(number)
num = number.clear() # clear the list 
print("list after clear:" , num)

# change the list element
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie" # change element at index 2 to Millie
print(names)

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[1:4] = ["juan", "Anastasia"]
print(names)

