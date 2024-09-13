list=[]
for i in range(5):
    ele=int(input("enter element"))
    list.append(ele)

print("before reversing",list)
revlist=[]
for i in list:
    revlist=[i]+revlist

print("after reversing",revlist)