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
print(d.getName())
print(d.getAge())
d1 = Dog("bruno", 4)
d.setName("Lion")
print(d.getName())


# Example 3

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getGrade(self):
        return self.grade


class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        # We can create any no. of attributes inside the class and no need to pass
        self.students = []

    def addStudents(self, student):
        if (len(self.students)) < self.maxStudents:
            self.students.append(student)
            return True
        return False

    def getAverage(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value/len(self.students)


s1 = Student("Avi", 19, 89)
s2 = Student("Ani", 19, 67)
s3 = Student("Sony", 19, 74)

course = Course("Science", 2)
course.addStudents(s1)
course.addStudents(s2)
print(course.students)
print(course.students[0].name, course.students[1].name)
print(course.getAverage())


# Inheritance
# Example1


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Im {self.name} and my age is {self.age} ")

    def speak(self):
        print("I shout like anything")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Mew")

    def show(self):
        print(
            f"Im {self.name} and my age is {self.age} and Im in {self.color} color")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Bill", 6)
c = Cat("Billi", 5, "White")
d = Dog("Tom", 10)
f = Fish("Bubble", 9)
p.show()
p.speak()
c.show()
c.speak()
d.show()
d.speak()
f.speak()


# Class Attributes


class Person:
    no_of_People = 0  # Class attributes
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.no_of_People += 1


p1 = Person("Tejaswini")
print(Person.no_of_People)
p2 = Person("Tara")
print(p2.no_of_People)

# Class methods


class Person:
    no_of_People = 0

    def __init__(self, name):
        self.name = name
        Person.add()

    @classmethod
    def printNo(cls):
        return cls.no_of_People

    @classmethod
    def add(cls):
        cls.no_of_People += 1


"""     @classmethod
    def no_of_People_(cls):
        return cls.no_of_People

    @classmethod
    def addPeople(cls):
        cls.no_of_People += 1 """


p1 = Person("Tejaswini")
print(Person.printNo())

p2 = Person("Tejaswini")
print(Person.printNo())


# Static method example

class statEx():
    @staticmethod
    def add5(x):
        return x+5


s = statEx()
print(s.add5(5))
