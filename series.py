def sum(x,n):
    total=1
    multi=x
    print(1,end=" ")
    for i in range(1,n+1):
        total=total+multi
        multi=multi*x
    print()
    return total
x=int(input("enter x value:"))
n=int(input("enter the number:"))
print(sum(x,n))



