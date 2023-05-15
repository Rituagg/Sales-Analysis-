import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('sales.csv')

#What time should we display advertisemens to maximize the likelihood of customer’s buying product?
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Order Date']=df['Order Date'].dt.round('H')
df['Time']=df['Order Date'].dt.hour
df=df.groupby('Time')['Quantity Ordered'].sum()
plt.plot(df.index,df.values)
plt.grid()
plt.show()
print(df)
# df.to_csv('sales1.csv',index=False)
print(df.info())