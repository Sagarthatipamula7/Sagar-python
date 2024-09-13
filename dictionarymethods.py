
student={"name":"sagar",
    "age":20,
    "marks":{
        "phy":78,
        "chem":89,
        "maths":99
    }
}
print(student)

#dict.keys() used to return keys of dictionary
print((list(student.keys())))

#dict.values() used to return all the values of keys
print(list(student.values()))

#dict.items() used to return all the key value pairs in dict
list=list(student.items())
print(list[0:])

#dict.get() used to return values of particular key. It can be done in two ways 
print(student["name"])
print(student.get("name"))

#print(student["name2"]) return error in case of using get() it will return None
print(student.get("name2"))

#dict.update() used to add key value pairs for dictionary
student.update({"city":"surat","height":5.4})
print(student)
