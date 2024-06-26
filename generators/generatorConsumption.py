import random

def generateData():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        reference= random.choice(["ACH01","ACH02","ACH03"])
        brand=random.choice(["Talesun","Suntech","Jinko","Risen"])
        power=random.randint(100,2000)
        city=random.choice(["Medellin","Bogota","Cali","Pereira","Manizales"])
        responsible=random.choice(["Sonia","Diego","Jose","Wilson","Carlos"])
        dato=[id,reference,brand,power,city,responsible]
        datos.append(dato)
    return(datos)
print(generateData())   

