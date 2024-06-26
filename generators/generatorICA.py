import random 

def generateDataICA():
    dataSurvey=[]
    for i in range(2000):
        data={}
        comuna=random.choice(["poblado:comuna 1","aranjuez:comuna 2","boston:comuna 3","robledo:comuna 4","belen:comuna 5","guayabal:comuna 6","campo amor:comuna 7","laureles:comuna 8","san javier:comuna 9","la america:comuna 10","floresta:comuna 11","castilla:comuna 12","santo domingocomuna 13","villa hermosa:comuna 14","candelaria:comuna 15","buenos aires:comuna 16","sin","-","nan"])
        ica=random.randint(10,100)
        date=random.choice(["2024-06-23","2024-06-25","2024-01-30","2024-07-31"])
        id=random.randint(1,50000)
        data=[comuna,ica,date,id]
        dataSurvey.append(data)
    return dataSurvey

generateDataICA()