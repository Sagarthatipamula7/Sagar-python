#The topic is about del keyword
class student:
    name="sagar"
    age=19
    def __init__(self,name):
        self.name=name

s=student("sagar")
print(s)
print(s.name)
del s
print(s)
print(s.name)
