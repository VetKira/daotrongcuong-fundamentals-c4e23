prices={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    
}

stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}



# for tenvatpham in (prices and stock) :
#     tenvatpham = input("ten mat hang : ") 
#     if tenvatpham == "banana" or tenvatpham =="apple" or tenvatpham =="orange" or tenvatpham =="pear" :
#         print("prices : ",prices[tenvatpham])
#         print("stock : ",stock[tenvatpham])
#         break
#     else : 
#         print("mat hang ban nhap hien k ton tai , xin vui long nhap lai ")
#         tenvatpham = input("ten mat hang : ")


total = 0
for i in (prices and stock):
    i = input("ten mat hang tinh tien : ") 
    tien = prices[i] * stock[i] # o day i la key cua dict prices vs stock
    print("gia mat hang la : ",tien)
    total= tien +total
print(total)



