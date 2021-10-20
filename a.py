import plotly.express as px
import csv
import pandas as pd
import numpy as np

def getdatasource(datapath):
    icecreamsales=[]
    coldrinksales=[]
    with open(datapath) as csvfile:
        d=csv.DictReader(csvfile)
        for row in d:
            icecreamsales.append(float(row["Temperature"]))
            coldrinksales.append(float(row["Ice-cream Sales( â‚¹ )"]))
    return {"x":icecreamsales,"y":coldrinksales}

def findcorrelation(datasource):
    c=np.corrcoef(datasource["x"],datasource["y"])
    print("The correlation coefficient is:"+str(c[0,1]))

def setup():
    datapath="icecream.csv"
    datasource=getdatasource(datapath)
    findcorrelation(datasource)

setup()