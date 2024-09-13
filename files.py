def replace():
      with open("practice.txt","r") as f:
            data=f.read()
      
      new_data=data.replace("java","python")
      print(new_data)
      with open("practice.txt","w") as f:
            f.write(new_data)
replace()
with open("practice.txt","r") as f:
      data=f.readline()
      print(data)
      data=f.readline()
      print(data)
      data=f.read(5)
      print(data)
      data=f.readlines(2)
      print(data)

