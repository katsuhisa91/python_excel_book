import pandas as pd

df = pd.read_csv('sample.csv', header=None)
df.loc[0] = ['10', '20', '30']
df.to_csv('sample2.csv', index=False, header=None)
