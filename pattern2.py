n=int(input("enter no of rows:"))
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")

    print()