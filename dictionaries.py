
#dictionaries is used to store all datatypes as key or value
#dictionaries are mutable
dict={
    "name" : "sagar",
    "age" : 19,
    "marks" : 89.0,
    "subjects" : ["maths","phy","chem"]
}
print((dict))
print(type(dict))

#adding dict to existing ones

dict["city"]="surat"
print(dict)

#dictionaries are mutable
dict["city"]="mumbai"
print(dict)

print(dict["name"])