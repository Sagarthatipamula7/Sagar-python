n=int(input("enter the number"))
a=0
print(a,end=" ")
b=1
for i in range(2,n+1):
    c=a+b
    print(c,end=" ")
    a,b=b,c