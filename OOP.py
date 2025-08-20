# Example 1

class Dog:
    def __init__(self):
        pass

    def bark(self):
        print("Dog Barks ")

    def addOne(self, x):
        return x+1


d = Dog()
d.bark()
print(d.addOne(5))

# Example 2


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name
        # return self.name


d = Dog("Tom", 3)
""" print(d.getName())
print(d.getAge()) """
""" d1 = Dog("bruno", 4) """
d.setName("Lion")
print(d.getName())
