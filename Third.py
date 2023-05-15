import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#what city sold the most products?
df=pd.read_csv('sales.csv')
'''
def ex(v):
    l=v.split(',')
    return l[1]
    df['City']=df['Purchase Address'].apply(ex)
'''
df['City']=df['Purchase Address'].str.split(',',expand=True)[1]
df=df.groupby('City')['Quantity Ordered'].sum().reset_index().sort_values('Quantity Ordered')
sns.catplot(x='City',y='Quantity Ordered',data=df,kind='bar')
plt.show()
print(df)
print(df.info())