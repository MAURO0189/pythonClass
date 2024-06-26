from generators.generatorConsumption import generateData

import pandas as pd 


def analysisData():
    datos= generateData()
    table= pd.DataFrame(datos,columns=["id","reference","brand","power","city","responsible"])
    table.to_csv("dataConsumer.csv", index=False)
    
analysisData()    