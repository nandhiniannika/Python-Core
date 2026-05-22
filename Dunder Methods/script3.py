class A:
    def __init__(self , x):
        self.x = x
    def __add__(self , o):
        return self.x + o
# obj = A(20)
# print(obj + 20)


class A:
    def __init__(self , x):
        self.x = x
    def __add__(self , o):
        if isinstance(o , int):
            return self.x + o
        if isinstance(o , A):
            return self.x + o.x
        else:
            print("Wrong Class")
            return 0

# obj = A(20)
# print(obj + 20)
# obj1 = A(50)
# obj2 = A(30)
# print(obj1 + obj2)
class A:
    def __init__(self , x , y , z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"x:{self.x} , y:{self.y} , z:{self.z}"
    def __repr__(self):
        return f"x:{self.x} , y:{self.y} , z:{self.z}"

    def __add__(self , o):
        if isinstance(o , int):
            return self.y + o
        elif isinstance(o , str):
            return self.x + o
        elif isinstance(o , A):
            return  self.x + o.x , self.y + o.y ,self.z + o.z
        else:
            print("Wrong Class")
            return 0
# s2 = s = A("Hello" , 20 , 10)
# s = A("Hello" , 20 , 20)
# s3 = A("Hello" , 20 , 20)
# print(s + "Hi")
# print(s + 20)
#
#
#
# print(s)
# print([s])


class Products:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"name : {self.name} , price:{self.price} , quantity:{self.quantity}"
class cart:
    def __init__(self):
        self.l = []
    def __add__(self , other):
         self.l.append(other)
         return self
    def __sub__(self, other):
        if other in self.l:
            self.l.remove(other)
        else:
            print("No items")
        return self
    def total_price(self):
        s = 0
        for i in self.l:
            s += i.price * i.quantity
        return s
    def __repr__(self):
        for i in self.l:
            print(i)
        print(f"total products:{len(self.l)}")
#
# p1 = Products("milk" , 2 , 2)
# c1 = cart()
# print(p1)
# print(c1)
# print(c1 + p1)


class Relation:
    def __init__(self,a):
        self.a = a
    def __gt__(self,other):
        return self.a > other.a
    def __lt__(self,other):
        return self.a < other.a
    def __ge__(self,other):
        return self.a >= other.a
    def __le__(self,other):
        return self.a <= other.a
    def __eq__(self, other):
        return self.a == other.a
# e1 = Relation(45)
# e2 = Relation(45)
# print(e1 > e2)
# print(e1 < e2)
# print(e1 >= e2)
# print(e1 <= e2)
# print(e1 == e2)
import math
class vector:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    def __sub__(self , other):
        return self.x - other.x
    def check(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __gt__(self , other):
        return self.check() > other.check()
    def __lt__(self , other):
        return self.check() < other.check()
    def __ge__(self , other):
        return self.check() >= other.check()

    def __le__(self , other):
        return self.check() <= other.check()
    def __eq__(self , other):
        return self.check() == other.check()
    def __str__(self):
        return f"{self.x} , {self.y}"
# v1 = vector(2 , 5)
# v2 = vector(5,2)
# v3 = vector(3,4)
# print(v1 + v2 + v3)
# print(v1 - v2)
# print(v1 > v2)
# print(v1 < v2)
# print(v1 >= v2)
# print(v1 <= v2)
# print(v1 == v2)
# print(v1)




class BankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self , amount):
        self.balance += amount
    def withdraw(self , amount):
        if self.balance>=amount:
            self.balance -= amount
        else:
            return f"Insufficient Balance"
    def __str__(self):
        return f"Account Holder :{self.account_holder} \n Balance :{self.balance}"
    def __add__(self , other):
        return self.balance + other.balance
    def __sub__(self, other):
        return self.balance - other.balance
    def __lt__(self, other):
        return self.balance < other.balance
    def __eq__(self, other):
        return self.balance == other.balance
    def __getattribute__(self, item):
        print(f"Accessing attribute {item}")
        return object.__getattribute__(self,item)
    def __setattr__(self, name, value):
        if name == "balance" and value < 0:
            print("Negative Balance is not allowed")
        else:
            return object.__setattr__(self , name , value)
# obj = BankAccount("Nandhini" , 10000)
# obj.deposit(10000)
# obj.withdraw(5000)
# print(obj)
# obj2 = BankAccount("Harshitha" , 1000)
# print(obj + obj2)
# print(obj - obj2)
# print(obj < obj2)
# print(obj == obj2)
# obj.balance = 1000000
# print(obj)




class Product:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"Product : {self.name} \n Price : {self.price} \n Quantity : {self.quantity}"
    def __add__(self,other):
        return self.total_price() + other.total_price()
    def __mul__(self , num):
        return self.price * num
    def __gt__(self , other):
        return self.total_price() > other.total_price()
    def __eq__(self , other):
        return self.price == other.price
    def __setattr__(self, name,value):
        if name == "price" and value <0:
            print("Price should be greater that 0")
        else:
            return object.__setattr__(self , name , value)
    def __getattr__(self, item):
        return f"Attribute not found {item}"
# obj = Product("Milk" , 20 , 5)
# obj2 = Product("Tea Packets" , 10 , 20)
# print(obj)
# print(obj2)
# print(obj + obj2)
# print(obj * 5)
# print(obj == obj2)
# print(obj > obj2)
# obj.price = 40
# print(obj.color)



class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks > 90:
            return "A"
        elif self.marks > 60:
            return "B"
        else:
            return "C"
    def __str__(self):
        return f"Student Name : {self.name} \n Marks : {self.marks} \n Grade :{self.grade()}"
    def __add__(self , other):
        return self.marks + other.marks
    def __truediv__(self, num):
        return self.marks / num
    def __lt__(self, other):
        return self.marks < other.marks
    def __ge__(self, other):
        return self.marks >= other.marks
    def __getattribute__(self, item):
        print(f"Accessing attribute of {item}")
        return object.__getattribute__(self , item)
    def __setattr__(self, name, value):
        if (name == "marks" and (value < 0 or value > 100)):
            print("Marks should be in range 0 to 100")
        else:
            return object.__setattr__(self, name, value)
# obj = Student("Nandhini" , 100)
# print(obj)
# obj2 = Student("Harshitha" , 99)
# print(obj2)
# obj2.marks = -99
# print(obj < obj2)
# print(obj >= obj2)
# print(obj / 5)




class Rectangle:
    def __init__(self , length , breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def __str__(self):
        return f"Length : {self.length} , Breadth : {self.breadth} , Area :{self.area()}"
    def __add__(self , other):
        return self.area() + other.area()
    def __sub__(self , other):
        return self.area() + other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __getattr__(self, item):
        return f"{item} is missing"
    def __setattr__(self, name, value):
        if (name == "length" and value < 0) or (name == "breadth" and value < 0):
            print("Length and Breadth should be greater than 0")
        else:
            return object.__setattr__(self, name, value)
# obj = Rectangle(100,200)
# print(obj)
# obj2 = Rectangle(50 , 25)
# print(obj2)
# print(obj + obj2)
# print(obj + obj2)
# print(obj + obj2)




































