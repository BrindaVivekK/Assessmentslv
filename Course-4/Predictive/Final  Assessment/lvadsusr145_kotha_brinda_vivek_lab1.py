# -*- coding: utf-8 -*-
"""LVADSUSR145_Kotha Brinda_Vivek_lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aENXG_aDWg72FR8yXKct8xLVp8GT2AzR

**KOTHA BRINDA VIVEK**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import dataset
df=pd.read_csv('/content/Fare prediction.csv')

df.head()

df.info()

df.describe()

numerical_cols=df.select_dtypes(include=['int64','float64']).columns
numerical_cols

corr_mat=df[numerical_cols].corr()
sns.heatmap(corr_mat,annot=True)

df.isnull().sum()

df.duplicated().sum()

df.drop_duplicates()

X=df.drop(columns=['fare_amount','pickup_datetime','key'])
y=df['fare_amount']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=110)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

from sklearn.metrics import mean_squared_error,r2_score
print("mse:",mean_squared_error(y_test,y_pred))
print("rmse:",mean_squared_error(y_test,y_pred,squared=False))
print("r2 score:",r2_score(y_test,y_pred))

from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

from sklearn.metrics import mean_squared_error,r2_score
print("mse:",mean_squared_error(y_test,y_pred))
print("rmse:",mean_squared_error(y_test,y_pred,squared=False))
print("r2 score:",r2_score(y_test,y_pred))

#for a model model to be good rmse,mse should be low and r2 score should be high
#hence random forest regressor predicts more accurately than linear regression
#has low mse and rmse than linear regression