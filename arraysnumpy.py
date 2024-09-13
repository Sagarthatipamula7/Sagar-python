#predifined functions of numpy package to create array
from numpy import *
arr=array([1,2,3,4,5])
arr1=array([1,2,3.0,4])
print(arr1)
print(arr)

#here 3 is a no of parts to divided and 15 is not excluded
arr=linspace(0,15,3)
print(arr)

arr=zeros(5)
print(arr)

arr=ones(5)
print(arr)

arr=arange(0,15,2)#it is just like a range funtion
print(arr)
print(type(arr))

arr=logspace(0,15,3)
print(arr)

