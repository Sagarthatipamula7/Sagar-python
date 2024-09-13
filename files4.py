with open("sagar.txt","w") as f:
    f.write("sagar is a good boy")
    print(f.tell())
    f.seek(9)
    print(f.tell())
with open("sagar.txt","r") as f:
    f.flush()
    data=f.read()
    
print(data)