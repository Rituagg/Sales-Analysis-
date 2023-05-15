import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('sales.csv')
#What product sold the most? Why do you think it sold the most?
df=df.groupby('Product')['Quantity Ordered'].sum().reset_index().sort_values('Quantity Ordered')
sns.catplot(x='Product',y='Quantity Ordered',data=df,kind='bar')
plt.xticks(rotation=90)
plt.grid()
plt.show()
print(df.info())
print(df)