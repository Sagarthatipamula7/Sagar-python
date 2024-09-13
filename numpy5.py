#other ways of creating arrays
from numpy import *
arr=array(zeros((3,3)))#null matrix
print(arr)
arr=array(ones((4,4)))
print(arr)
arr=array(eye(3))#indentity matrix
print(arr)
arr=array(random.rand(5))#generates random elements
print(arr)
arr=array(random.randn(5,3))
print(arr)
#fixed valued array
arr=array(full([3,3],45))
print(arr)
#arange the elements of array according to the given range and steps
arr=array(arange(10,90,3))
print(arr.shape)
a=arr.reshape(3,3,3)
print(a)
#linespace in this elements are arranged according to the fixed spaces
arr=array(linspace(3,9,6))#6 elements are created between 3 and 9
print(arr)