#multi level inheritance

class A:
    def display(self):
        print("A class")
class B(A):
    def b(self):
        print("B class")
class C(B):
    def c(self):
        print("c class")
        
c=C()
c.display()
c.b()
b=B()
b.display()