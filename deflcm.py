def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if(greater%x==0 and greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm

num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
print("The lcm of",num1,"and",num2,"is:",lcm(num1,num2))