# 1. Írjon programot, mely kiírja a képernyőre 1-10 ig a számok reciprokát!

for i in range(0,11):
    try:
        print(1/i)
    except ZeroDivisionError:
        print("A nullának nincs reciproka, mert nincs olyan szám, amellyel a nullát szorozva 1-et kapunk.")
    

# 2. írj programot, mely beolvassa a hatvány alapját és a kitevőt, és kiírja a hatványértéket!

alap=int(input("Kérek egy hatvány alapot! "))
kitevo=int(input("Kérek egy kitevőt! "))
eredmeny=alap**kitevo
print(f"{alap}^{kitevo} = {eredmeny}")

# 3. Írj programot, ami csak pozitív számot hajlandó beolvasni.

szam=int(input("Kérek egy pozitív egész számot! "))

if szam<0:
    print("Ez a szám nem pozitív egész szám! Menj, tanulj még egy kis matekot! :D")
else:
    print("A(z) " +str(szam)+ " " "pozitív egész szám. Köszi.")

# 4. írj programot, mely bekér két számot és eldönti mennyi a távolságuk a számegyenesen!

# 5. írj programot, mely addig kér számokat a billentyűzetről amig összegük kisebb mint 100!

ismet=True
while(ismet):

    szam1=int(input("Kérek egy számot! "))
    szam2=int(input("Kérek egy másik számot is! "))

    if szam1+szam2==100:
        ismet=False
        print("A számok összege 100, így vége a programnak")
            
    else:
        print("A számok összege nem 100, dolgozz még egy kicsit!")
    
 
# 6. írj programot, melyben addig dobunk kockával amig nem sikerül 6-ost dobni. A dobásokat jelenítsd meg!

import random
ismet=True

while(ismet):

    for dobas in range(1,7):
        if dobas==6:
            ismet=False
            print("Hatost dobtál. Gratulálok, de most ezzel vége a programnak.")
            
        else:
            print("Még nem dobtál hatost, játszhatsz még egy kicsit.")

# 7. Írj programot, mely eldönti egy számról, hogy prímszám-e!

prim=int(input("Kérek egy számot! "))
prim2=prim

if prim%1==0 and prim%prim2==0:
    print("A szám" " "+str(prim)+ " ""prímszám.")
elif prim%1!=0 and prim%prim2!=0:
    print("A szám" " "+str(prim)+ " ""nem prímszám.")
else:
    print("A szám" " " +str(prim)+ " ""nem prímszám.") 
    
    