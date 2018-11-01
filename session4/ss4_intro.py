# person = ["Kira","Hai Phong","WRU",22,4,257,False]

# person={} # neu co ngoac{} python se hieu day la dictionary
# print(person)
# print(type(person))

# person={
#     "name": "kira" #key:value
# }
# print(person)
# print(type(person))


person={
    "name":"kira",
    "place":"hai phong",
    "age": 22,
}
# print(person)

# person["girlfriend"] = 257 #[key]=value
# print(person)
# print(person["name"]) # hoac dat i = " name " r thay i vao


# key = " name"
# if key in person:
#     print(person[key])
# else:
#     print("not found")

#update : 
# person["age"] = 23
# print(person)

#xoa :
del person["age"]
print(person)

#list thi theo index , con diction thi theo key