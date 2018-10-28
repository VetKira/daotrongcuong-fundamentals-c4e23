yob_str = input("year of birth = ") #yob string se la input(.....
while not yob_str.isdigit(): # doi if thanh while se duoc nhieu lan , if chi duoc 1 lan ma thoi
    print("ban nhap sai")
    yob_str = input("year of birth = ")
yob = int(yob_str)
age = 2018- yob
print(age)
# y nghia cua vong lap while o day , yob dung ket hop vs not thanh false , thanh vong lap vo dung 1 lan dung lai
# neu ma yob_str false ket hop vs not thanh true , thanh vong lap vo han