str="sagar is a good boy"
s=str.split()
print(s[::-1])

#reversing words and internal string
str="sagar"
s=reversed(str)
ot="".join(s)
print(ot)


str="sagar is a bad boy"
s=str.split()
temp=" "
i=len(s)-1
while i>=0:
    temp=temp+s[i]+" "
    i-=1
print(temp,end=" ")

#reversing internal strings
str="welcome to bhai's club"
s=str.split()
list=[]
for word in s:
    list.append(word[::-1])

print(list)