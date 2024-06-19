import pandas as pd
from generators.generatorICA import generateDataICA

def buildDataIca():
    # Generate dataFrame using ICA
    dataIca = generateDataICA()
    dataFrameIca = pd.DataFrame(dataIca, columns=["comuna","ica","fecha","id"])
    dataFrameIca.to_csv("datosIca.csv", index=False)
    print(dataFrameIca)

buildDataIca()    