str=input("enter the string of sentences:")
s=str.split()
words=[]
for i in s:
    words.append(i[::-1])

output=" ".join(words)
print(output)
