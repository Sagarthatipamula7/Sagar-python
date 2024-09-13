n=int(input("enter the number"))
sum=0
r=0
m=n
while n>0:
    r=n%10
    sum=sum+r*r*r
    n=n//10

if sum==m:
    print("armstrong number")
else:
    print("not an armstrong number")