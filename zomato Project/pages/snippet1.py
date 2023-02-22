import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataEngineering import dataEngineering

df = pd.read_csv('zomato.csv')
df1 = pd.read_csv('zomato.csv')

# Task-1
# Data Engineering
df1['rupees'] = 0
df1 = dataEngineering(df1)

df1['Country'] = ''

for i in df1.index:
  if( df1.iloc[i]['Country Code'] == 14 ):
    df1.iloc[i,-1] = 'Australia'
  elif( df1.iloc[i]['Country Code'] == 1 ):
    df1.iloc[i,-1] = 'India'
  elif( df1.iloc[i]['Country Code'] == 30 ):
    df1.iloc[i,-1] = 'Brazil'
  elif( df1.iloc[i]['Country Code'] == 37 ):
    df1.iloc[i,-1] = 'Canada'
  elif( df1.iloc[i]['Country Code'] == 94 ):
    df1.iloc[i,-1] = 'Indonesia'
  elif( df1.iloc[i]['Country Code'] == 148 ):
    df1.iloc[i,-1] = 'Newzealand'
  elif( df1.iloc[i]['Country Code'] == 162 ):
    df1.iloc[i,-1] = 'Philippines'
  elif( df1.iloc[i]['Country Code'] == 166 ):
    df1.iloc[i,-1] = 'Qatar'
  elif( df1.iloc[i]['Country Code'] == 184 ):
    df1.iloc[i,-1] = 'Singapore'
  elif( df1.iloc[i]['Country Code'] == 189 ):
    df1.iloc[i,-1] = 'South Africa'
  elif( df1.iloc[i]['Country Code'] == 208 ):
    df1.iloc[i,-1] = 'Turkey'
  elif( df1.iloc[i]['Country Code'] == 214 ):
    df1.iloc[i,-1] = 'UAE'
  elif( df1.iloc[i]['Country Code'] == 215 ):
    df1.iloc[i,-1] = 'United Kingdom (UK)'
  elif( df1.iloc[i]['Country Code'] == 216 ):
    df1.iloc[i,-1] = 'United States'

# Changes for Indias's costly Cuisines
# print(len(df1[df1['Currency']=='Dollar($)']))