import pandas as pd
import matplotlib.pyplot as plt # type: ignore
from generators.generatorICA import generateDataICA

def buildDataIca():
    # Generate dataFrame using ICA
    dataIca = generateDataICA()
    dataFrameIca = pd.DataFrame(dataIca, columns=["comuna","ica","fecha","id"])
    dataFrameIca.to_csv("datosIca.csv", index=False)
    print(dataFrameIca)

    #generando graficas de los datos por comuna 
    #dataClearByComuna=dataFrameIca.groupby("comuna")["ica"].mean()
    #plt.figure(figsize=(20,20))
    #dataClearByComuna.plot(kind="bar", color="green")
    #plt.show()

buildDataIca()    