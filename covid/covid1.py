#Topic: Corona File 
#-----------------------------
#libraries

import pandas as pd
url='https://raw.githubusercontent.com/datasets/covid-19/master/time-series-19-covid-combined.csv'

df = pd.read_csv(url)
df.head()
df.columns

df.index
df.values
df.sort_values('Deaths')
df.sort_values('Deaths', ascending=True)

df.Deaths.sort_values()
df.Deaths.sort_values(ascending=False)
df.tail(5)

df[['Country/Region', 'Deaths']]
df.groupby('Country/Region').sum()
df.groupby(['Country/Region']).sum()
df[df.columns[1:4]] 
df.iloc[:, 0:2]
df.iloc [0:2, 1:3] 
df.loc[1:3, ['Country/Region', 'Deaths']] 
df[['Country/Region', 'Deaths']].groupby(['Country/Region']).sum().plot()
df[['Country/Region', 'Deaths']].groupby(['Country/Region']).sum().plot.bar(rot=180)

