import pandas as pd
import temp

df = pd.read_csv('GooglePlayStore_wild123.csv')



df['Rating'] = df['Rating'].fillna(-1,inplace = True)

def make_size(prise):
    if prise[-1] == '$':
        return float(prise[:-1])

    return -1
df['Price'] = df['Price'].apply(make_size)
df['Profit'] = df['Installs'] * df['Price']
print(df[df['Type'] == 'Paid']['Size'].max)

temp = df.pivot_table(columns = 'Category',index = 'Content Rating' , values = 'Reviews',aggfunc = 'max')
print(temp['EDUCATION', 'FAMILY', 'GAME'])

