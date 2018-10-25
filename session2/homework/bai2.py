n = int(input("hay nhap so ngau nhien :"))
s = 1
for i in range(1,n+1): # la n+1 la vi , vd 9! thi n+1 = 10 nghia la bat dau tu 1 den truoc 10 la 9
    s *= i # nhan va gan hay chinh la nhan cong dan , giai thua

print(" giai thua cua", n , "la" ,s)