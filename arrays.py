import array as arr
vals=arr.array('i',[1,2,3,4,5,6,7])
print(vals)
new_arr=arr.array(vals.typecode,(a*a for a in vals))
print(new_arr)

from array import *
vals=array('i',[1,2,3,4,5])
print(vals)
for e in vals:
    print(e)
vals=array('u',['a','b','c','d'])
print(vals)
#creating new array
