import os
import pandas as pd
import numpy as np

path=r'D:\Sales Analysis Project'
files=os.listdir(fr'D:\Ritu Python\Sales Analysis Project\Sales Data')
print(files)
df=pd.DataFrame()
for file in files:
    monthly_sale=pd.read_csv(fr'{path}\Sales Data\{file}')
    df=pd.concat((df,monthly_sale))
# print(df)

print(df.info())
print(df.to_csv(fr'{path}\sales.csv'))
#firstly we will remoove all rows having all null values
df=df.dropna(how='all')
# print(df)
#correcting datatype of orderid first
df['temp']=df['Order ID'].str.isdigit()
df=df.loc[(df.temp==True)]
df=df.drop(columns='temp')
#checking if there is any incorrect value in OrderID other than int
df['Order ID']=df['Order ID'].astype(np.int64)
print(df)
print(df.info())
df.to_csv('sales.csv',index=False)
df.to_csv(fr'D:\Sales Analysis Project\Corrected_data.csv')
