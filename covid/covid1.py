#Topic: Corona File 
#-----------------------------
#libraries

import pandas as pd
url='https://raw.githubusercontent.com/datasets/covid-19/master/time-series-19-covid-combined.csv'

df = pd.read_csv(url)
df.head()
