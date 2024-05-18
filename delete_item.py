import pandas as pd

df = pd.read_csv('output2.csv')


for index, row in df.iterrows():
    if (row[0].find('cap') != -1):
        df.drop(index, inplace=True)
df.to_csv('output2.csv', index=False, encoding='utf-8-sig')