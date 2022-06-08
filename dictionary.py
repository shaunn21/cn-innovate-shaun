

#! Dictionaries

#? keys values
#? 1:"key":"value"
#? .items = key and Value
#? .keys = key
#? .value = value



test_dict = {
    "football":"man utd",
    "football2":"man city",
    "football3":"liverpool"
}
print (test_dict["football"])

test_dict.update({"football": "chelsea"})
test_dict.update({"football2": "tottenham"})
test_dict.update({"football3": "newcastle"})

print (test_dict["football2"])


for j in test_dict.keys():
    print(j)
for j in test_dict.values():
    print(j)
for j in test_dict.items():
    print(j)        


#! set default
test_dict.setdefault ("man utd",True)
test_dict.setdefault ("man city","wolves")
#! cant use it to update an existing key

#! remove from dict
test_dict.pop ("man utd")
#! ###########

#! Del keyword
del test_dict("football")
#! ###########