try:
    n1=int(input())
    n2=int(input())
    result=n1/n2
    print(result)
except ZeroDivisionError:
    print("exception is handled")
    
else:
    print("result printed")
finally:
    print("tera baap hu mein beta mujhe chodkar kaha jahega")