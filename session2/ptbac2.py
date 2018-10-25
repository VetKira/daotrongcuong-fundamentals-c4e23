a= int(input("a= "))
b= int(input("b= "))
c= int(input("c= "))
delta = b*b-(4*a*c)
print(delta)
if delta <0:
    print("pt vo nghiem")
elif delta == 0: # 2 dau bang , 1 dau bang la gan gia tri , 2 dau la dem ra so sanh
    print("pt co 1 nghiem")
    x= (-b)/(2*a)
    print(x)
elif delta >0:
    print("pt co 2 nghiem")
    x1= ((-b)+delta**0.5)/(2*a)
    x2= ((-b)-delta**0.5)/(2*a)
    print(x1,x2)

