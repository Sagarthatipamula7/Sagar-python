#@staticmethod is not used for modifying,changing the variables,The variables and 
#methods are static 
#where as in @classmethod we can modify the parent methods and variables
class A:
    name="sagar"
    def changename(self,newname):
        self.name=newname
a=A()
a.changename("sai")
print(a.name)#sai
print(A.name)#sagar


class A:
    name="sagar"
    def changename(self,newname):
        A.name=newname#changed another way is @classmethod
a=A()
a.changename("sai")
print(a.name)#sai
print(A.name)#sagar

class A:
    name="sagar"
    @classmethod
    def changename(cls,newname):
        cls.name=newname
a=A()
a.changename("sai")
print(a.name)#sai
print(A.name)#sai

