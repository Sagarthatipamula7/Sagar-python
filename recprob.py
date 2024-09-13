def list_elements(list,idx):
    if idx==len(list):
        return
    else:
        print(list[idx])
        list_elements(list,idx+1)
a=[1,2,3,4,5]
list_elements(a,0)
    