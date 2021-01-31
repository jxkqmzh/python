from numpy.core.defchararray import split
from pandas.core.indexes import period
from pandas.core.indexes.datetimes import date_range
import numpy as np
import pandas as pd

print('hello world!')

df = pd.DataFrame({'id':[1001,1002,1003,1004,1005,1006],
                'date':pd.date_range(start='2020/01/02', periods=6),
                'city': ['beijing', 'SH', 'Guangzhou', 'Shenzhen', 'shanghai', 'BEIJING'],
                'age': [23,44,54,32,34,32],
                'categrate': ['100-A', '100-B', '110-A', '110-C','210-A','130-F'],
                'price': [1200, np.nan, 2133,5433,np.nan, 4432]},
                columns=['id', 'date', 'city', 'categrate', 'age', 'price'])

print(df)
print(df.shape)
print('*'*50)
print(df.info())
print('*'*50)
print(df['id'].dtype)
print(df.isnull())

print(df.columns)
print(df)
df = df.fillna(value=0)
print('*'*50)
print(df)

df = df.rename(columns={'categrate':'categrate-size'})
print('*'*50)
print(df)


df1 = pd.DataFrame({'id':[1001,1002,1003,1004,1005,1006,1007,1008],
                    'gender':['male','female','male','female','male','female','male','female'],
                    'pay': ['Y','N','Y','N','Y','N','Y','N'],
                    'm-point':[10,12,20,40,40,40,30,20]})

print(df1)

df_inner = pd.merge(df, df1, how='inner')
print(df_inner)
df_inner = df_inner.set_index(df.id)
print('*'*50)
print(df_inner)

print('*'*50)
df = df_inner.sort_values(by=['age'])
print(df)

df = df.sort_index()
print(df)

df['group'] = np.where(df['price'] > 3000, 'high', 'low')
print(df)


df.loc[(df['city'] == 'beijing') & (df['price']>1000),'sign'] = 1
print(df)


df_split = df.loc[1001:1003]
print('df_split = \n', df_split)

df = df.set_index('date')
print(df)

print('df.iloc = ', df.iloc[[0,1,3],[0,2,4]])
df1 = df.loc[df['city'].isin(['beijing', 'Guangzhou'])]
print('df1 = \n', df1)

df1.loc['2020-01-31'] = [ 1111, 'beijing', '111-A' ,22, 1111, 'male', 'y' , 100, 'low' ,1]
print('df1 = \n', df1)