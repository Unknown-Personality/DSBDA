import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv('IRIS.csv')
#print(df)

#Data cleaning

"""
print(df.head())
print(df.tail(10))

print(df.isnull())
print(df.isna())

print(df.isnull().any())

print(df.isna().sum())
"""

"""
#1>>Data Integration
#print(df)
df1=df.iloc[:,:3].reset_index()
df2=df.iloc[:2,3:].reset_index()
#print(df1)
#print(df2)

df3=df1.merge(df2,on='index',how='inner')
#print(df3)

#drop duplicate

df3.drop_duplicates(subset=['index'],inplace=True)
print(df3)
"""
#2>>>Data Transformation


data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, None, 90, 65, 88],
    'Science': [78, 80, None, 75, 82],
    'History': [70, 68, 75, None, 78]
}

df = pd.DataFrame(data)
print(df)

df1=df[['Math','Science','History']]
#df1=df1.mean()
print(df1)

df2=df1.fillna(df1.mean())
print(df2)

scaler=MinMaxScaler()
df3=scaler.fit_transform(df2)
print(df3)


#3>>>Error Handling


df.dropna(subset=['Math', 'Science'], inplace=True)
df.dropna(axis=1, inplace=True)

#4>>>build model

df=pd.read_csv('heart.csv')

x=df.drop(df['target'])
z=df['target']
y=z.head(301)
print(df)
print(x)
print(y)
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print(y_pred)

from sklearn.metrics import accuracy_score,confusion_matrix
print(accuracy_score(y_test,y_pred))

print(confusion_matrix(y_test,y_pred))
