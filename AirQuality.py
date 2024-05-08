import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,Binarizer,MinMaxScaler

from sklearn.linear_model import LinearRegression


from sklearn.model_selection import train_test_split

air=pd.read_csv(r'path',sep=",")

#Data Cleaning
'''print("Values Present for Each Column:")
print(air.count())
print("Total NaN values for Each Column: ")
print(air.isna().sum())
print("Mathematical Description of Dataset : ")
print(air.describe())
print("Informatio : ")
print(air.info())'''

#A=air.dropna() #drops null values and result store in A
#A=air.fillna(0)
#print(A.head(50))


#Error Correcting
#method-1
'''A=air.bfill()
print(A.head(50))
A=air['Ozone'].replace(np.NaN,air['Ozone'].mean())
print(A.head(50))
print(air.describe())'''

#Data Transform

'''scaler=StandardScaler() #initialize scaler
B=scaler.fit_transform(air)
print(pd.DataFrame(B).describe())'''

'''scaler=MinMaxScaler()
B=scaler.fit_transform(air)
print(pd.DataFrame(B).describe())'''

'''bin=Binarizer(threshold=0.5)
B=bin.fit_transform(B)
print(pd.DataFrame(B).describe())'''


#Model Building
air['Ozone']=air['Ozone'].replace(np.NaN,air['Ozone'].mean())
A = air.fillna(air.mean())

'''X=A['Ozone'].values
X=X.reshape(-1,1)
#print(X)

Y=A['Temp']
model=LinearRegression()
model.fit(X,Y)

print(model.score(X,Y)*100)
print(model.predict([[128]]))

import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.show()'''

train,test=train_test_split(A,test_size=0.20)
print(len(train))
print(len(test))
