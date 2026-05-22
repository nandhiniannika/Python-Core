# class A:
#     def m1(self):
#         print("A class")
# class B(A):
#     def m1(self):
#         print("B Class")
#         super().m1()

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
obj.m1()
print(D.mro())
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
c1 = C()
c1.m1()

