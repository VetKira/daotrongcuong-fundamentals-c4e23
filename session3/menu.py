# item1= "kr fourze"
# item2= "kr build "
# item3= "kr zio"
# item4= "kr drive"
# item5= "kr exaid"

# items=[]#empty list
# print(items)
# print(type(items))

# items =["kr fourze"]
# print(items)

# items=["kr fourze ", "krzio","krghost"]
# print(items)

# items.append('krbuild') #append la them
# print(items)
# print(*items, sep=",") #SEP la separate

# mylist=["krghost"]
# print(*mylist)
# new=input("nhap them: ")
# mylist.append(new)
# print(*mylist , sep=" | ")

# mylist=["krghost","krdrive","krbuild"]

# mylist[1]="krdive final form"
# print(mylist)
mylist=["krghost","krdrive","krbuild"]
# mylist.pop(1) #pop la xoa theo vi tri
# print(mylist)
# mylist.remove("krbuild") # xoa theo noi dung
# print(mylist)

print(mylist)
i=int(input("index :"))
new_value = input("new value: ")
mylist[i]= new_value
print(mylist)

