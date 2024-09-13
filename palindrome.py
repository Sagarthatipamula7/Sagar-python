n=int(input("enter the value"))
r=0
rev=0
m=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=int(n/10)

if rev==m:
    print("palindrome")
else:
    print("not a palindrome")