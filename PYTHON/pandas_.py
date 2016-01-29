# Toujours bien faire attention à ne pas nommer son fichier du même nom qu'un module.
# Ici si mon script s'appelle "pandas", avec import pandas la machine ne sait plus quoi importer...


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[34,32,65,49,43,51],
             'Bounce_Rate':[54,76,86,25,64,19]}
df = pd.DataFrame(web_stats)
##print(df.head())
##print(df)
##print(df.tail())
##print(df.tail(2))

##df2 = df.set_index('Day')
##print(df.head())
##
##df.set_index('Day', inplace= True)
##print(df.head())

print(df['Visitors']) #To get infos on a particular column.
print(df.Visitors)

print(df.Visitors.tolist())
print(df[['Bounce_rate','Visitors']])

