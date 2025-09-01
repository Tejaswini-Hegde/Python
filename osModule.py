import os
from datetime import datetime

# Change directory
os.chdir("/home/tejaswini/Desktop")

# Get current working dir
# print(os.getcwd())

# List directories present in current folder
# print(os.listdir())

# Creating a directory
""" os.mkdir("Pract_Python")
print(os.listdir()) """

# Creating Folder structure
""" os.makedirs("PractPython1/Trying")
print(os.listdir()) """

""" # Remove Dir
os.rmdir("Pract_Python")
print(os.listdir())

os.removedirs("PractPython1/Trying")
print(os.listdir())
 """

""" # Created a file
filename = "Testing.txt"
f = open(filename, 'w')
f.write("Hello")
f.close
print(os.listdir())

newName = "Test.txt"
os.rename(filename, newName)
print(os.listdir()) """

print(os.stat("Test.txt"))  # Shows all the details
print(os.stat("Test.txt").st_mtime)            # Shows modified time
print(os.stat("Test.txt").st_size)             # Shows size
mod_time = os.stat("Test.txt").st_mtime
x = datetime.fromtimestamp(mod_time)
print(x.strftime("%H %M %S : %D"))        # 19 02 26 : 09/01/25
print(x.strftime("%H %M %S : %b %d %y"))  # 19 02 26 : Sep 01 25
print(x.strftime("%H %M %S : %B %d %Y"))  # 19 02 26 : September 01 2025
