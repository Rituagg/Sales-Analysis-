import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#What was the best month for sales? How much was earned that month?
df=pd.read_csv('sales.csv')
#sale each day=quantity ordered*price each
df['SED']=df['Quantity Ordered'] * df['Price Each']

#converting order date in date time format
df['Order Date']=pd.to_datetime(df['Order Date'])
df['month']=df['Order Date'].dt.month_name()
df=df.groupby('month')['SED'].sum().reset_index().sort_values('SED')

sns.catplot(x='month',y='SED',data=df,kind='bar')

plt.show()
# #check columns
# print(df.columns)
# df.to_csv('sales2.csv',index=False)
# # print(df.info())
print(df)