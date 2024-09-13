#creates file if not exits if exits truncate and write
with open("sagar.txt","w") as f:
    f.write("sagar is a good boy\nHe is from surat\nAt present he is pursuing Btech in mlritm college")
#read the existing file 
with open("sagar.txt","r") as f:
    data=f.read()
    print(data)
#add characters at end of the file
with open("sagar.txt","a") as f:
    f.write("\nhe wanted to become a bussinessman")
#overwrites the existing file and no truncate 
with open("sagar.txt","r+")as f:
    f.write("shiva")
with open("sagar.txt","r+")as f:
    data=f.read()
    print(data)
#truncate the the existing file and creates file if not exist
with open("sagar.txt","w+") as f:
    f.write("sagar is a fool")
with open("sagar.txt","a+") as f:
    f.write("\nchinali sali")
with open("sagar.txt","w") as f:
    f.writelines(["sagar is a good boy\n","kranthi is intelligent one"])
    