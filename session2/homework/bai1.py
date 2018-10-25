h = int(input("nhap chieu cao cua ban theo cm : "))
w = int(input("nhap can nang cua ban theo kg : "))
h1 = h/100
BMI = w/(h1*h1)
print(" so BMI cua ban la :", BMI)
if BMI<16 :
    print("severely")
elif BMI<18.5 :
    print("underweight")
elif BMI<25 :
    print("normal")
elif BMI<30 :
    print("overweight")
else : 
    print("obese")