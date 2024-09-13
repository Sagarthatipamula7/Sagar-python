#multi level inheritance
class A:
    a="sagar bhai"
class B:
    b="sai bhai"
class C(A,B):
    c="kranthi bhai"

c=C()
print(c.c)  
print(c.a,c.b)  