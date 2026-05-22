# Q1. Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.

class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        if self.marks > 45:
            print("Passed")
        else:
            print("Failed")

# obj1 = Student("Nandhini" , 85);
# obj2 = Student("Vaishnavi" ,44)
# obj1.is_passed()
# obj2.is_passed()

# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.

class Employee:
    company = "TechCrop"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_company(cls,new_name):
        cls.company = new_name
# obj =Employee("Vaishnavi")
# Employee.change_company("cvCorp")
# print(obj.company)


# Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.

class MathOps:
    @staticmethod
    def is_even(num):
        return num%2 == 0

# obj = MathOps()
# print(obj.is_even(40))

# Q4. Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

class Car:
    wheels = 4
    def __init__(self , mileage):
        self.mileage = mileage
    def display(self):
        print(f"Wheels : {Car.wheels} \n Mileage : {self.mileage}")
    @classmethod
    def change(cls , n):
        cls.wheels  = n
# obj = Car(54)
# obj.display()
# obj.change(3)
# obj.display()

# Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

class Temperature:
    def __init__(self , celsius):
        self.celsius = celsius
    @staticmethod
    def change(celsius):
        a = (celsius * (9 / 5)) + 32
        return a
    def show_conversion(self):
        f = Temperature.change(self.celsius)
        print(self.celsius)
        print(f)

obj =  Temperature(45)
obj.show_conversion()

