class student:
    name="Sagar Thatipamula"
    def __init__(self):
        print("default constructor")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=student()
s1=student("sagar",19)
print(s1.name,s1.marks)