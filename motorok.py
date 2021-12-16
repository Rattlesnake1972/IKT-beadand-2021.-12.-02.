print("\n")

print("Motorok: legkisebb végsebesség")

print("\n")

class Motorok:
    def __init__(self, motornév="", sebesség=0):
        self.motornév=motornév 
        self.sebesség=sebesség
        
Mocik=[]

for i in range(3):
    motornév=input("Add meg egy motortípus nevét! ")
    sebesség=int(input("Hány km/h a végsebessége? "))
    egymotor=Motorok(motornév,sebesség)
    Mocik.append(egymotor)

print("\n")
 
for egymotor in Mocik:
    print("A(z) {0} végsebessége {1} km/h." .format(egymotor.motornév,egymotor.sebesség))

leglassubbMocik=Mocik[0]
for item in Mocik:
    if item.sebesség<leglassubbMocik.sebesség:
        leglassubbMocik=item
        
print("\n")
        
print("A leglassabb motor a három közül: " +leglassubbMocik.motornév+ ", mert annak csak " +str(leglassubbMocik.sebesség)+ "km/h a végsebessége.")

print("\n") 