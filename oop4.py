class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print("Hi",self.name,"Your avg score of all subjects is:",sum/len(self.marks))
list=[100,99,97]
s=student("sagar",list)
s.name="yogi"#mutable
s.avg()