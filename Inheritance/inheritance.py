# class A:
#     def m1(self):
#         print("A class")
# class B(A):
#     def m1(self):
#         print("B Class")
#         super().m1()
from abc import abstractmethod
from typing import override


# obj = B()
# obj.m2()


class A:
    def m1(self):
        print("A")
        super().m1()
class B:
    def m1(self):
        print("B")
        super().m1()
class C:
    def m1(self):
        print("C")

class D(A,B,C):
    def m1(self):
        print("D")
        super().m1()
obj=D()
# obj.m1()
# print(D.mro())
#a1=A()
#a1.m1()



class A:
    x = 0
    def m1(self):
        print("A class")
class C:
    def m1(self):
        a1 = A()
        a1.m1()
        print("C class")
# c1 = C()
# c1.m1()



# class Animal with a method sound().Create a derived class Dog that overrides the sound() method.Demonstrate method overriding.

class Animal:
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    def sound(self):
        print("woffffffff")

# d = Dog()
# d.sound()

# • Create class A with method show().Create class B(A) that overrides show() and also calls the parent method using super().

# class A:
#     def show(self):
#         print("A class")
# class B(A):
#     def show(self):
#         print("B class")
#         super().show()

# b = B()
# b.show()

# • Create multi-level inheritance with classes A → B → C, each having a method display() printing the class name.Create object of C and call display(), showing method resolution.
class A:
    def display(self):
        print("A")
class B(A):
    def display(self):
        print("B")
        super().display()
class C(B):
    def display(self):
        print("C")
        super().display()
# c = C()
# c.display()

# • Implement hierarchical inheritance using a base class Vehicle and two child classes Car and Bike, each defining a method wheels().
class Vehicle:
    def wheels(self):
        print("Wheels of Vehicles")
class Car(Vehicle):
    def wheels(self):
        print("4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("2 wheels")

# bike = Bike()
# bike.wheels()
# car = Car()
# car.wheels()

# • Create class Employee with an instance method salary().Create class Manager(Employee) that overrides salary() and adds an incentive.Demonstrate both outputs.

class Employee:
    def salary(self):
        print("50000")
class Manager(Employee):
    def salary(self):
        print("30000")
        print("incentives: 100000" )

# obj = Manager()
# obj.salary();
#
# emp = Employee()
# emp.salary()



#  Create class University with a class variable and a class method. Inherit it into class College and access the parent’s class variable from the child class.

class University:
    x = 100
    def display(self):
        print("University")
class College(University):
    def display(self):
        print("College")

# obj = College()
# print(obj.x)



# • Create class MathOps with a static method add(a, b). Create class AdvancedOps(MathOps) and use the static method without overriding it.
class MathOps():
    @staticmethod
    def add(a , b):
        return a + b
class AdvancedOps(MathOps):
    pass
obj = AdvancedOps.add(10,20)
# print(obj)

# • Create two classes Father and Mother, both defining a method skills(). Create class Child(Father, Mother) and check which skills() runs using MRO.
class Father:
    def skills(self):
        print("Father Skills")
class Mother:
    def skills(self):
        print("Mother Skills")
class Child(Father,Mother):
    pass
obj = Child()
# print(obj.skills())
# • Create an abstract class Shape with an abstract method area(). Create class Rectangle(Shape) that implements the area() method.

class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
obj = Rectangle(10 , 20)
print(obj.area())

# • Create class Person with a constructor __init__(name). Create class Student(Person) with constructor __init__(name, roll). Use super() to call the parent constructor.




