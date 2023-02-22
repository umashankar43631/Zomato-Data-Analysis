import pandas as pd
import numpy as np

class ChangeCurrency:
  def __init__(self):
    pass
  def getIndex(self, df1, currencyName):
    # returning iterator
    return df1[df1['Currency'] == currencyName ].index[:]
  def changeToIndian(self, df1, currencyName):
    if(currencyName == 'Indian Rupees(Rs.)'):
      return "you are converting rupee to rupee, its not needed"
    for i in self.getIndex(df1,currencyName):
      if(currencyName == 'Botswana Pula(P)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 6.42
      elif(currencyName == 'Brazillian Real(R$)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 16.06
      elif(currencyName == 'Dollar($)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 81.47
      elif(currencyName == 'Emirati Diram(AED)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 22.18
      elif(currencyName == 'Indonesian Rupiah(IDR)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 0.0055
      elif(currencyName == 'NewZealand($)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 52.88
      elif(currencyName == 'Pounds(專)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 100.99
      elif(currencyName == 'Qatari Rial(QR)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 22.37
      elif(currencyName == 'Rand(R)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 4.76
      elif(currencyName == 'Sri Lankan Rupee(LKR)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 0.22
      elif(currencyName == 'Turkish Lira(TL)'):
        if(df1.iloc[i, -1] == 0 ):
          df1.iloc[i, -1] = df1.iloc[i]['Average Cost for two']* 4.33
    
