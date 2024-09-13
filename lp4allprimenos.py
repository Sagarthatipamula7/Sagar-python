start=int(input("prime no's want from :"))
end=int(input("prime no to:"))
print("prime no's starts from",start,"ends at",end)
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        
        else:
            print(num)
