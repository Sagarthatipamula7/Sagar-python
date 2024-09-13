def dups(list):
    duplist=[]
    sinlist=[]
    for ele in list:
        c=list.count(ele)
        if c>=2:
            duplist.append(ele)
        else:
            sinlist.append(ele)
    dups=set(duplist)
    print(dups)
    print(sinlist)
    
l=[1,2,2,3,3,4,5,6,6]
dups(l)