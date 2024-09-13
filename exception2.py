def age_cal(num):
    if num<18:
        raise ValueError("not eligible for vote")
    
try:
    age=int(input("enter the age:"))
    age_cal(age)
    
except ValueError:
    print("exception handled")
    
else:
    print("eligible for voting")