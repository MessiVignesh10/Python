my_dict ={
    "name" : "Vignesh",
    "age" : 22,
    "Mark" : "LastMark"
}

another_dict ={
    "name" :"Saravanan",
    "Age" : 22,
    "Mark" : "FirstMark"
}

print(my_dict)
print(my_dict["Mark"])
print(my_dict.get("age"))
print(my_dict.keys())
my_dict ["age"] =10
print(my_dict)

#update command in dictionary

my_dict.update({"rank":1})
print(my_dict)
newDict = my_dict.copy()
print("-------------------------------------------")
print(newDict)

for a in another_dict.values():
    print(a)

for b in another_dict.keys():
    print(b)