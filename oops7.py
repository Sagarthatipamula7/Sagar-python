#This topic is about private and public classes
#public class
class student:
    name="sagar"
    age=21
s=student()
print(s.name,s.age)

#private class,objs and variables
class student:
    def __init__(self,name,age):
        self.name=name
        self.__age=21#we cannot access this var outside the class
        print(self.__age)
    def __hello(self):#private method used for internal operation
        print("nitish bhai")
    def welcome(self):
        self.__hello()
         
s=student("sagar",21)
print(s.name)
s.welcome()



