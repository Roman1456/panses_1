import pandas as pd

df = pd.read_csv('GoogleApps (3).csv')

#print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())

free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)