#class and instance attributes
class student:
    name="sagar"#class attributes/objects
    age=20
    def __init__(self,name,age):
        self.name=name#object attributes/objects
        self.age=age#obj att>cls att
s1=student("nishith",19)
print(s1.name,s1.age)