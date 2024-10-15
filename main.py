import pandas as pd
import temp

df = pd.read_csv('GoogleApps (3).csv')

temp = df.pivot_table(columns = 'Category',index = 'Content Rating' , values = 'Reviews',aggfunc = 'max')
print(temp['EDUCATION', 'FAMILY', 'GAME'])
