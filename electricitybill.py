#<100 units no charge
#>100 and <200 $5 per unit
#>200 $10 per unit
amt=0
units=int(input("enter no of units used"))
if units<=100:
   print("no charge")
elif units>100 and units<=200:
   amt=(units-100)*5
else:
   amt=500+(units-200)*10

print("electricity bill is",amt)

