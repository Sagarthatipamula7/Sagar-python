#aquiring properties of parent class to the class is known as inheritance
# single level inheritance
# multi level inheritance
# multiple inheritance

#single level inheritance
class Animal:
    @staticmethod
    def eat():
        print("eating")
    @staticmethod
    def sleep():
        print("sleeping")
class dog(Animal):
    def bark(self):
        print("dog class")
        
d=dog()
d.eat()
d.sleep()
d.bark()    