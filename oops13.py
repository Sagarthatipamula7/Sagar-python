#super method used for accessing super class variables and methods

class A:
    def display(self):
        print("A class")
class B(A):
    def b(self):
        print("B class")
class C(B):
    def c(self):
        print("c class")
        super().display()
        
c=C()
c.display()
c.b()
b=B()
b.display()
c.c()