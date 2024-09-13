def sum(list):
    clist=[]
    length=len(list)
    clist=[sum(list[0:x] for x in range(length+1))]
    print(clist)

lists=[10,20,30,40,50]
sum(lists)
        