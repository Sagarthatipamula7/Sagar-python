#list is built in datatype used to store values of different datatypes
#list is mutable we can modify and change
list=['1','2','3','4']
print(list)
list[0]=90
print(list)


#slicing of list
list=['1','2','3','4','5']
print(list[:6])

#methods of list
#append method which is used to add the elements at the end
list=['a','b','c','d']
list.append('e')
print(list)

#sort method is used for sortion the elements either in asc or desc order
list=['a','d','e','c','b']
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#remove method is used for removing 1st occurence of ele
list=['a','b','c','d','e']
list.remove('e')
print(list)

#pop method is used for removing ele in particular index
list=['1','2','3','7','4']
list.pop(3)
print(list)

#insert method is used for inserting ele at particular index
list=['1','2','3','4','5']
list.insert(6,'6')
print(list)

#indexing is not possible in list

#reverse method
list=[1,2,3,4,5]
list.reverse()
print(list)

list.append(1)
print(list)

print(list.count(1))
list.pop(5)
print(list)

list.sort()
print(list)

list.insert(5,6)
print(list)

print(min(list))
print(max(list))

list.clear()
print(list)


