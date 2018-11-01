luong = [
    {
        "name": " Huy",
        "hours": 30,
        "vndper1":50,
    },
    {
        "name":"Quan",
        "hours":20,
        "vndper1":40,
    },
    {
        "name":"Duc",
        "hours":15,
        "vndper1":35,
    }
]

# for p in luong:
#     print(p['hours'])

# for p in luong:
#     luongper1 = p["hours"]*p["vndper1"] #o day la p vi p da pha list va o day p la dict hours va vnd la key
#     print(" luong tung nguoi la : ", luongper1)

tong =0
for p in luong:
    luongper1 = p["hours"]*p["vndper1"]
    tong = luongper1 + tong
print(tong)
    
    