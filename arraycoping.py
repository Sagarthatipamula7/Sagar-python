from numpy import *
arr1=array([1,2,3,4,5])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
#in order to not to get same address we use view()
arr1=array([1,3,5,7])
arr2=arr1.view()#if we use copy() method modification is not done in both arrays
arr1[1]=9#copied in both arrays called shallow copying
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)

