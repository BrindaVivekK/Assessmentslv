# -*- coding: utf-8 -*-
"""LVADSUSR145_Kotha_Brinda_Vivek_IA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qjtSKh8WR3MjmkRBTv4ep0ZwGZgyWHNq

**KOTHA BRINDA VIVEK**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix,r2_score,mean_squared_error,accuracy_score,f1_score,precision_score,recall_score

df=pd.read_csv('/content/expenses.csv')

df.head()

df.info()

df.describe(include="all")

df.shape

df.isnull().sum()

df['bmi'].isnull().dropna()

df

df.isnull().sum()

df.dropna(axis=0)

df.isnull().sum()

df.shape

#outliers managing
#to handle outliers,we have to remove or change the outliers
#outliers are those who are not in interquartile range(iqr=q3-q1)
numerical_columns=df.select_dtypes(include=['int64','float64']).columns
numerical_columns

for column in numerical_columns:
  plt.figure(figsize=(10,5))
  sns.boxplot(x=df[column])
  plt.xlabel=column
  plt.title(f'Boxplot of {column}')
  plt.show()

#2 Encoding
categorical_columns=df.select_dtypes(include=['object']).columns
categorical_columns

for column in categorical_columns:
  df[column]=LabelEncoder().fit_transform(df[column])

df

#feature selection
numerical_columns=df.select_dtypes(include=['int64','float64']).columns

corr_matrix=df[numerical_columns].corr()
corr_matrix

sns.heatmap(corr_matrix,annot=True,fmt='.2f')

"""smoking has high correlation for insurance charges"""

#4test train split
X=df.drop(['charges','bmi'],axis=1)
y=df['charges']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.30, random_state = 10)

#scaling
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

mse=mean_squared_error(y_test,y_pred)
print("mse",mse)
rmse=mean_squared_error(y_test,y_pred,squared=False)
print("rmse",rmse)
r2=r2_score(y_test,y_pred)
print("r2 score",r2)

