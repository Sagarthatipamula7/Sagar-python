#creating null set 
collection=set()
print(type(collection))
#add method
collection.add(1)
collection.add("sagar")
collection.add(("subject",19))
print(collection)

#remove method
collection.remove("sagar")
print(collection)

#set pop method is used to remove element randomly from the set
collection.pop()
print(collection)

#clear method
collection.clear()
print(collection)

#union method 
set1={1,2,3,4,5,6,7}
set2={6,7,8,9}
print(set1.union(set2))

#intersection method
print(set1.intersection(set2))

print(set1.difference(set2))

print(set2.issubset(set1))