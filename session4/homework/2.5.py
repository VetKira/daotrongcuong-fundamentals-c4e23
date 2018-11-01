sheep = [5,7,300,90,24,50,75]
print("Hello ,my name is Kira , and these are my sheep sizes : ",sheep, sep ="\n")
for i in range (3):
    i +=1
    print("month", i)
    big = max(sheep)
    print("now my biggest sheep has size : ", big," let's shear it .")

    x = sheep.index(big)
    sheep[x] =8
    print("after shearing , here is my flock: ",sheep, sep ="\n")

    for j in range(len(sheep)):
        sheep[j] +=50
    print("one month has passed , now here is my flock : ",sheep,sep="\n")

    if i==3:
        x=sum(sheep)
        a = x*2
        print("my flock has size in total : ",x)
        print("i would get ", x, " *2$ = ",a,"$"  )