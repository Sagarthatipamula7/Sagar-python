str=input("enter any string")
i=len(str)-1
temp=" "
while i>=0:
   temp=temp+str[i]
   i-=1

print(temp)

#using for loop
s=input("enter the string")
temp=" "
for i in range(len(s)-1,-1,-1):
   temp=temp+s[i]

print(temp) 