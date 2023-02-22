import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from snippet1 import df1
# Task -1
d1=df1.groupby(["Currency"])['Currency'].count()
fig=px.pie(d1,values=list(df1['Currency'].value_counts()), names= list(df1['Currency'].unique()), title = "Indian Currency vs Other Currency")
fig.show()

