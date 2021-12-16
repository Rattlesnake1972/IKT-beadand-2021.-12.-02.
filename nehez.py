print("\n")

print("A legnehezebb állat")

print("\n")

class Állatfaj:
    def __init__(self, fajnév="", tömeg=0):
        self.fajnév=fajnév 
        self.tömeg=tömeg
        
Allatok=[]

for i in range(3):
    fajnév=input("Add meg egy állatfaj nevét! ")
    tömeg=int(input("Hány kilogramm a tömege egy példánynak? "))
    egyAllat=Állatfaj(fajnév,tömeg)
    Allatok.append(egyAllat)
    
for egyAllat in Allatok:
    print("A(z) {0} tömege {1} kg" .format(egyAllat.fajnév,egyAllat.tömeg))
    
legnehezebbAllat=Allatok[0]
for item in Allatok:
    if item.tömeg>legnehezebbAllat.tömeg:
        legnehezebbAllat=item
        
print(legnehezebbAllat.fajnév) 