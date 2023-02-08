n = int(input())
p = input()

x = 0
y = 0
cara = "ESWN"
a = 0
mapa = {"E":0,"S":0}

for i in p:

    if i == "S":
        if cara[a] == "E":
            mapa["E"] += 1
        elif cara[a] == "S":
            mapa["S"] -= 1
        elif cara[a] == "W":
            mapa["E"] -= 1
        elif cara[a] == "N":
            mapa["S"] += 1
    else:
        a+=1
    if a == len(cara):
        a = 0

x = mapa["E"]
y =  mapa["S"]

print(x,y)













    

