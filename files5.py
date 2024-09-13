with open("nish.txt","w") as f:
    f.write("asalam malekum\nmalekum salam\neid mubarak")
with open("nish.txt","r") as f:
    data=f.read()
with open("nish.txt","r") as f:
    data1=f.readline()
with open("nish.txt","r") as f:
    data2=f.readlines()
    
print(data)
print(data1)
print(data2)