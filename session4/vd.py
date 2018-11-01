
culua={
    "cc": "con co` ru",
    "lmao": "laugh my ass off",
    "lol" : " deo phai lien minh ,laugh out loud",
    "asap": "as soon as possible",
    "dcm" : " Dinh Cong Manh",
    "fuck": " ewww oi , ns bay nao",
    "kimochi": " tuy thuoc vao hoan canh , hihihihi :3"

}

while True: 
    x = input(" moi nhap vao :")
    if x in culua:
        print("dich nghia la :",culua[x])
        
    else :
        print("xao lon k co gi vui vi the chung ta khong nen xao lon")
        n = input(" the tao hoi may co muon them vao khong  (y/n): ").upper()
        if n=="y":
            value= input(" nhap y nghia :")
            culua[x] = value #<diction>[key]=value
        elif n =="n":
            print( " the thi cut")
            break
        else : 
            print("may bi ngu a` ")
            break

        



