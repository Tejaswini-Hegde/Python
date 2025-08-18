# name = input("Please enter your name: \n")
""" print("Hello !!", name, "Welcome to practice session!!")
x, y, z = input("Enter X,Y,Z values respectively").split()
print("X is", x)
print("Y is", y)
print("Z is", z)
 """

""" print(dir(name))
print(name.upper()) """

##############
# String Operations:

""" sample = "Python Programming"
print(sample[0])
print(sample[-1])
print(sample[0:4])
print(sample[0:])
print(sample[:3])
print(sample[:])
print(sample[0:-1])
print(sample[-5])
print(sample[3:-3]) """

# Formatting

""" first = "Tejaswini"
last = "Hegde"
full = f"{first} {last}"
print(full)
full = f"{len(first)} {2+5}"
print(full) """

# print(dir(str))

""" x = int(input("X :"))
y = 2
y += x
print(y)
print(f"x is : {x} , y is: {y}") """

""" temperature = 20
if temperature > 30:
    print("temperature is considerably high")
elif temperature > 25:
    print("temperature is slightly high")
else:
    print("It's cold")

print("ended if") """

""" age = 18
message = "Yes" if age >= 18 else "No"
print(message)
print("yes" if age < 18 else "no") """

""" high_income = True
high_credit = True
student = False
if high_income and high_credit and not student:
    print("Eligible")
else:
    print("Not Eligible") """

# Loop

""" for i in range(3):
    print("Attempt", i+1, (i+1)*"*")

print(10*"*")

for i in range(1, 4):
    print("Attempt", i, (i)*"*")

print(10*"*")

for i in range(1, 10, 2):
    print("Attempt ", i, i*"*")

print(10*"*") """
"""
success = True
for i in range(3):
    print(i+1)
    if success:
        print("Done")
        break """


""" number = int(input("Enter the number\n"))
j = 0
for i in range(1, number):
    if i % 2 == 0:
        j += 1
        print(i)
print("Total number of even numbers", j) """

"""
def increment(number, by):
    return (number+by)


print(increment(2, by=1)) """

""" # Printing F shape
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print("*"*i)

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    for j in range(i):
        print("*", end="")
    print() """

""" # Find Largest number n the list
num = int(input("Enter number of items you want to insert into list : "))
list1 = []
for i in range(num):
    l1 = int(input(f"Item {i} :"))
    list1.append(l1)
print("User input is ", list1)
max = list1[0]
for i in list1:
    if i > max:
        max = i
print("Max is ", max) """

# Matrix of 3X3

""" matrics = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrics[0])

for row in matrics:
    for i in row:
        print(i, end=" ")
    print() """

# List operations

""" n = int(input("Enter Number of items you want to add to the list : \n"))
list1 = []
for i in range(n):
    num = int(input(f"Enter the {i} th element : "))
    list1.append(num)
print(f"Your list is {list1}")
print("Perform actions\n1:Add\n2:Remove\n3:Insert at specific position\n4:Reverse\n5:Sort\n6:Exit")
while True:
    ch = input("Enter choice : ")
    try:
        if ch == "1":
            item = int(input(f" Enter the item to be added : "))
            list1.append(item)
            print(list1)
        elif ch == "2":
            item = int(input(f" Enter the item to be removed : "))
            list1.remove(item)
            print(list1)
        elif ch == "3":
            i = int(input(f" Enter the index at which item to be added : "))
            item = int(input(f" Enter the item to be added : "))
            list1.insert(i, item)
            print(list1)
        elif ch == "4":
            # list1.reverse()
            list = list1[::-1]
            print(list)
        elif ch == "5":
            list1.sort()
            print(list1)
        elif ch == "6":
            exit
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print("Unknown error occured :", e) """

# Write program to remove duplicate items in list without creating another list

""" n = int(input(f"Enter number of elements to add to list : "))
list1 = []
for i in range(n):
    item = input(f"Enter item {i} : ")
    list1.append(item)
print(f"Your list is {list1}")

list1.sort()
l1 = len(list1)

for i in range(len(list1)-1, 0, -1):
    print(len(list1))
    if list1[i] == list1[i-1]:
        print("Removed : ", list1[i-1])
        del list1[i]
        print(list1)

print("Final list is : ", list1) """

# Using another list

""" list1 = [1, 5, 3, 3, 7, 7, 2]
unique = []
for item in list1:
    if item not in unique:
        unique.append(item)
print(f"Final list {unique}") """

# Loop decrement and increment

""" n = 5
print("Decrement")
for i in range(n, 0, -1):
    print(i)
print("inrement")
for i in range(1, n+1, 1):
    print(i, end=" ")
print() """

# Tuples

""" tup = ()
n = int(input("Enter no. of elements : "))
for i in range(n):
    s = input(f"Enter item at {i} : ")
    tup += (s,)
print(tup) """

# Unpacking
""" tup = (1, 2, 3, 4, 5)
a, *b, c, d = tup
print(a, b, c, d) """

# Dictionary

""" n = int(input("Enter no. of values : "))
dict = {}
for i in range(n):
    key = input("Enter Key ")
    val = input("Enter Value ")
    dict[key] = val
print(dict)

print(dict["name"])
print(dict.get("name"))
 """

""" # Sets

set1 = set()  # Declaring empty set
print(set1)
set1 = set("Tejaswini Hegde")
print(set1)

print(dir(set))

n = int(input("Enter no. of values : "))
s1 = set()
for i in range(n):
    item = input(f"Enter {i} element : ")
    s1.add(item)

print("your set is : ", s1)
i = input("Enter item to be deleted : ")
s1.remove(i)

print("your set is : ", s1)
 """

"""f = open("myData", 'r')
print(f)

print(f.read())

print("Reading firstline")

print(f.readline())
 """
""" f1 = open("textFile", 'w')

s = "Im writing code in VS Code"
f1.write(s)

f1 = open("textFile", 'r') """
""" 
print(f1.read())

f1 = open("textFile", 'a')
f1.write("started logging")


f1 = open("textFile", 'r')

print(f1.read()) """

f1 = open("myData", 'r')
f2 = open("textFile", 'a')
for data in f1:
    f2.write(data)
