import plotly.express as px
import csv
import pandas as pd

with open("icecream.csv") as csvfile:
    d=csv.DictReader(csvfile)
    figure=px.scatter(d,x="Temperature",y="Ice-cream Sales( â‚¹ )")
    figure.show()