# list=[1,2,3,4,5,6,7]
# end=len(list)
# i=0
# while i<end:
#     print(list[i])
#     i+=1


# list=[1,2,3,4,5,6,7]
# end=len(list)
# for i in range(end):
#     print(list[i])


#searching the element
list=[10,20,30,40,50,60,70,80]
x=int(input("enter the number"))
end=len(list)
count=0
for i in range(end):
    if(list[i]==x):
        print("element found at index",count)
        break
    count+=1
