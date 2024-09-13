#the four pillars of oops concept is
# abstraction
# encapsulation
# polymorphism
# inheritance
#1.abstraction
#Hiding implementation details of a class and showing the essential features to the user
class account:
    def __init__(self,acc_no,pin):
        self.acc_no=False
        self.pin=False
    def display(self):
        self.acc_no=True
        self.pin=True
        print("displayed successfully")

acc=account("12345",1983)
acc.display()

#encapsulation
#wrapping data and funtions into a single unti(object)
class student:
    name="Thatipamula sagar"
    age=21
    
s=student()
print(s.name,s.age)
    