sheep = [5,7,300,90,24,50,75]
print("Hello ,my name is Kira , and these are my sheep sizes : ",sheep, sep ="\n")

big = max(sheep)
print("now my biggest sheep has size : ", big," let's shear it .")

x = sheep.index(big)
sheep[x] =8
print("after shearing , here is my flock: ",sheep, sep ="\n")

for i in range(len(sheep)):
    sheep[i] +=50
print("one month has passed , now here is my flock : ",sheep,sep="\n")