import random
cara = 0
cruz = 0

for i in range(20):
    lanza = random.choice(["cara","cruz"])
    if lanza == "cara":
        cara+=1
    elif  lanza == "cruz":
        cruz+=1

print(cara ,"cara",  cruz ,"cruz")
