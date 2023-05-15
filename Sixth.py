import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from collections import Counter

df=pd.read_csv('sales.csv')
#What products are most often sold together?
df=df[['Order ID','Product']]
# df['temp']=df['Order ID'].duplicated(keep=False)
df=df.loc[(df['Order ID']).duplicated(keep=False)]
df['grouped']=df.groupby('Order ID')['Product'].transform(lambda x:','.join(x))
c=Counter()
row_list=[]
li=df['grouped']
for i in li:
    row_list=i.split(',')
    c.update(Counter(combinations(row_list,3)))
l=c.most_common(20)
for item in l:
    print(item)




df.to_csv('Sales2.csv')
# print(df)
