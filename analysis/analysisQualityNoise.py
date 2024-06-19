import pandas as pd 
from generators.generatorDecibelios import generateDecibelios

def buildDataDecibelios():
    decibelios = generateDecibelios()
    dataFrameDecibelios = pd.DataFrame(decibelios, columns=["id","levelNoise","comuna"])
    dataFrameDecibelios.to_csv("Noise.csv", index=False)
    print(dataFrameDecibelios)

buildDataDecibelios()    
