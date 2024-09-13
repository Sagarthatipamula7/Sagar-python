class student:
    name="sagar"#class attributes
    age=19
    marks=90
    def student(self):#self is a reference of object
        pass
        print("default constructor")
    def __init__(self,name,age):#constructorf
        self.name=name#obj attributes
        self.age=age
    def welcome(self):#method
        print("welcome to python language")
    def display(self):
        print("displaying the method")
s=student("yogi",20)
print(s.name,s.age,s.marks)
s.welcome()
s.display()