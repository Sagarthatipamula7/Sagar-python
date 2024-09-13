# from math import *
# def finding_gcd(x,y):
#     print("Gcd of",x,"and",y,"is:",gcd(x,y))
# n1=int(input("enter the number1:"))
# n2=int(input("enter the number2:"))
# finding_gcd(n1,n2)

#using loops
def finding_gcd(x,y):
    gcd=1
    n=min(x,y)
    for i in range(1,n):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
n1=int(input("enter the number1:"))
n2=int(input("enter the number2:"))
print("gcd of",n1,"and",n2,"is:",finding_gcd(n1,n2))