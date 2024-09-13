n=int(input("enter n value"))
for i in range(n+1):
    if i%2==0:
        i+=1
        continue

    print(i,end=" ")
    i+=1

print( )


i=1
while i<=10:
    if i%2!=0:
        i+=1
        continue
    
    print(i,end=" ")
    i+=1