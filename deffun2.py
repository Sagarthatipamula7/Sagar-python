def convert_to_inr(n):
    price=n*86
    return price

i=int(input("enter the money in usd:"))
output=convert_to_inr(i)
print(output)