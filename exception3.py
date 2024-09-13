def age_cal(num):
    assert num<18
    print("not eligible")

try:
    n=int(input())
    age_cal(n)

except:
    print("eligible for voting")
        