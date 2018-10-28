password = input("nhap password :")
while True:

   
    if len(password)<8 :
        print(" dai hon 8")
    elif password.isalpha():
        print(" phai chua ca so")
    elif password.isupper() \
  or password.islower()\
   or password.isdigit() : #phai dung or vi dung and thi phai thoa man tat ca dieu kien and no ms chiu in ra print , con k thi loi k chiu in
        print("phai co ca hoa lan thuong va so")
    
    else :
        print("dang nhap thanh cong ")
        break  
    password = input("nhap password :")

    #password = input("nhap password :")
    #while not (len(password)>8)\
 #and password.isalpha()\
  #and password.isupper() \
 # and password.islower()\
  # and password.isdigit():
       


     
    