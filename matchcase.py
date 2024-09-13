def arithmetic_operation(n):
    a=int(input("enter the number 1:"))
    b=int(input("enter the number 2:"))
    match n:
        case 1:return a+b
        case 2:return a-b
        case 3:return a*b
print("\n1.add\n2.sub\n3.mul")
y=int(input("enter the choice:"))
x=arithmetic_operation(y)
print(x)       