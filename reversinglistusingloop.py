list=[1,2,3,4,5]
print("before reversing",list)
temp=[]
for i in list:
    temp=[i]+temp

print("after reversing the list",temp)