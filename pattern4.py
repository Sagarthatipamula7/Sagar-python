n=int(input("enter the no of rows:"))
for i in range(n):
    for j in range(i+1):
         print(" ",end=" ")
    for j in range(i,n):
        if i==0 or i==j or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()