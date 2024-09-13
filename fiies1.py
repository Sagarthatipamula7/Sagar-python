def find():
    with open("practice.txt","r") as f:
        data=f.read()
        word="programming"
        if word in data:
            return "found"
        else:
            return -1
print(find())