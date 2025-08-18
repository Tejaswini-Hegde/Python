""" def createArr(row, col):
    array = []
    for i in range(row):
        row = []
        print(f"Enter {i} th row : ")
        for j in range(col):
            item = int(input(f"Enter {i},{j} element: "))
            val = row.append(item)
        array.append(row)
    return array


result = createArr(2, 3)

for row in result:
    print(row) """

# using numpy

import numpy as np


def createArray(row, col):
    total = row*col
    print(f"Enter {total} elements to fit into {row}X{col} array :")
    arr = []
    for i in range(total):
        val = int(input(f"Element {i+1}: "))
        arr.append(val)
    arr1 = np.array(arr).reshape(row, col)
    return arr1


row = int(input("Enter no. of rows : "))
col = int(input("Enter no. of columns : "))

result = createArray(row, col)
print(result)

# add, multiply and exponential
print("adding 5")
print((result)+10)

print("Multiply by 2")
print((result)*2)

print("Exponential of 3")
print((result)**3)

print("Find max")
print(np.max(result))
print("Find min")
print(np.min(result))
print("Find mean")
print(np.mean(result))
