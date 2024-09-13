dict={}
dict.update({"name":"sagar",
             "age":19,
             "city":"surat"})
print(dict)
keys=dict.keys()
sorted_keys=sorted(keys)
print(sorted_keys)
keys_as_values={value:key for key,value in dict.items()}
print(keys_as_values)