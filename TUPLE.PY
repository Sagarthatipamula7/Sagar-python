#tuple is build in datatype which is immutable
#modification is not possible in tuples
tup=(1,2,3,4,5)
print(tup)
print(tup[2])
print(type(tup))
t=list(tup)
t[0]=9
s=tuple(t)
print(s)
#tup[0]=9 not possible

#tuple methods
#index method is used t0 return ele first occurance particular index
tup=(1,2,4,5)
print(tup.index(5))

#count method is used for counting no of times occurance
tup=(1,2,3,4,5,6,7,8,1,1,1,1,1,1,1,1,1,1,1)
print(tup.count(1))
