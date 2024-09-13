str=input("enter the string:")
n=int(input("enter the index:"))
y=list(str)
y.pop(n)
print("".join(y))

str=input("enter the sring:")
n=int(input("enter the index:"))
for i in range(len(str)):
    if str[i]!=str[n]:
        print(str[i],end="")