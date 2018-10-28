
items = ["T-shirt", "sweater"]

n= input("welcome to our shop , what do u want (c,r,u,d)?")
while True:
    if n==("c"):
        new = input("enter new items: ")
        items.append(new)
        print("our items : ",*items, sep =" | ")
        n= input("welcome to our shop , what do u want (c,r,u,d)?")
        
    elif n==("r"):
        print("our items : ",*items, sep= " | ")
        n= input("welcome to our shop , what do u want (c,r,u,d)?")
        
    elif n==("u"):
        i = int(input("update position : "))
        new_1 = input("new items : ")
        items[i] = new_1
        print("our items : ",*items , sep = " | ")
        n= input("welcome to our shop , what do u want (c,r,u,d)?")
        
    elif n==("d"):
        j= int(input("delete position : " ))
        items.pop(j)
        print("our items : ", *items ,sep = " | ")
        n= input("welcome to our shop , what do u want (c,r,u,d)?")
        
    else : 
        print(" just choose c , r , u , d")
        n= input("welcome to our shop , what do u want (c,r,u,d)?")





