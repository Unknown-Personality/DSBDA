import pandas as pd

df=pd.read_csv(r'path',sep=';')
#print(df.head())
#print(df.shape)

#Subset Creation
'''df1=df[['Page total likes','Type']].loc[0:15]
df2=df[['Page total likes','Type']].loc[16:30]
df3=df[['Page total likes','Type']].loc[31:50]

print(df1)
print(df2)
print(df3)'''


#Merging
'''df4=pd.concat([df1,df2,df3])
print(df4)'''

#sorting
'''print(df.head(50))
sort=df.sort_values('like',ascending=True)
print(sort.head(50))'''


#transpose
'''trans=df.T
print(trans.head())
print(df.shape)'''

#reshaping
pivot=pd.pivot_table(df,index=['Type','Category'],values='like')
print(pivot.head(40))



