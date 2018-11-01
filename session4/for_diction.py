person ={
    'name': ' cuong',
    'age' : '22',
}

p2 = {
    "name": " dung",
    "age": "21",
}

# for x in person: # in tat ca key trong dicti person
#     print(x)

# for k in person.keys(): #tuple ~ list
#     print(k, person[k]) 

# for v in person.values():
#     print(v)

# for k , v in person.items():
#     print (k,v)


# p_list =[]
# p_list.append(person)
# p_list.append(p2)
# print(p_list)
# p = p_list[0]
# print(p)
# print(p['age']) # or lam cach duoi
# print(p_list[0]['age']) # p_list la 1 list vi truy cap theo chi so 0 con p_list[0] la 1 dict vi truy cap theo key

# for p in p_list:
#     print(p)
#     print("-------")
#     print(p['age'])



p_list =[ # day la cach 1 phat duoc luon k can bien trung gian person , p2 nua
    {
    'name': ' cuong',
    'age' : '22',
},
{
    "name": " dung",
    "age": "21",
}
]
