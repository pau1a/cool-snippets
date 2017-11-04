import pandas as pd
import numpy as np
df = pd.read_csv('prescription.csv',low_memory=False).set_index('PracticeCode')
prac = pd.read_csv('prac.csv',low_memory=False)
prac['Practice Code']=prac['Practice Code'].astype(str)
prac.set_index('Practice Code',inplace=True)
df['PracticeCodeCopy']=df.index
df_filtered=pd.DataFrame()
df_filtered['Practice']=df['PracticeCodeCopy'].unique()
df_filtered['Total Practice Costs']=0
df_filtered.set_index('Practice',inplace=True)
new=df.groupby(['HealthBoardCode','PracticeCode'])
for name,group in new:
    prac_cost=df['GrossIngredientCost'][df['PracticeCodeCopy'] == name[1]]
    costsum=prac_cost.sum()
    df_filtered['Total Practice Costs'].loc[name[1]]=costsum
complete=pd.merge(df_filtered, prac, how='outer', left_index=True, right_index=True)
final=complete[['Practice Name','Total Practice Costs']].sort_values(by=['Total Practice Costs'],ascending=False).dropna()
print(final)
