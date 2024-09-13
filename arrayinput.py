from array import *
arr=array("i",[])
n=int(input("enter the length of array:"))
for i in range(n):
     ele=int(input("enter the next element:"))
     arr.append(ele)
print(type(arr))
print(arr)
x=int(input("enter the element for search:"))
for i in range(n):
    if arr[i]==x:
        print("element at the index:",i)
print(arr.index(x))