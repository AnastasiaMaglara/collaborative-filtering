from scipy import spatial
import pandas as pd
import numpy as np
import math
from ratingPrediction import Predictor

user='u'

#2. Function:
#def correllation(a, b):
#    return 1 - spatial.distance.correlation(a, b)

def pearson(df, a, b):
    df = df.replace(0, np.NaN)
    mean_a = df[a].mean()
    mean_b = df[b].mean()
    df = df.replace(np.NaN, 0)
    sum_a = np.sum(np.fromiter((pow(df[a][i] - mean_a,2) for i in df.index),float))
    sum_b = np.sum(np.fromiter((pow(df[b][i] - mean_b,2) for i in df.index),float))
    sum = np.sum(np.fromiter(((df[a][i] - mean_a) * (df[b][i] - mean_b) for i in df.index),float))/math.sqrt(sum_a * sum_b)
    return round(sum, 6)


df = pd.DataFrame([[4, 4, 4], [0, 2, 3]], columns=['u', 'v', 'z'], index=['V1', 'V2'])
print('Ratings of users\n',df)
#1. compute correlation with method pearson
#print(df.corr('pearson'))

#2. compute the correlation distance
#print(pd.DataFrame(df.corr(method=correllation)))

df2=pd.DataFrame(columns=df.columns, index=df.columns)
for i in list(df):
     for j in list(df):
         df2[i][j]=pearson(df,i,j)
print('Similarity table:\n',df2)

for ind in df2.index:
   if df2.loc[user,ind] <= 0:
       df = df.loc[:,df.columns != ind]
if not df.loc[:,df.columns != user].empty:
    print('Nearest neighbors to', user,':\n', df.loc[:, df.columns != user])
    print('The predicted rating:\n',Predictor.prediction(user, df.index.values[1], df2, df))
else:
    print('There is not match user with',user)