def finding_word():
    with open("practice.txt","r") as f:
        data=f.read()
    word="learning"
    data=True
    line=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if word in data:
                return line
            line+=1
    return -1
print(finding_word())