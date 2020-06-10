from scipy import spatial
import pandas as pd
import numpy as np
from ratingPrediction import Predictor

def cosine(a, b):
    return 1 - spatial.distance.cosine(a, b)

user= 'u'
df = pd.DataFrame([[4, 4, 4],[0, 2, 3]], columns=['u', 'v', 'z'], index=['V1', 'V2'])
print('Ratings of users:\n', df ,'\n')

df2 = pd.DataFrame(df.corr(method=cosine))
print('Similarity table:\n', df2 ,'\n')

for ind in df2.index:
   if df2.loc[user,ind] <= 0.5:
       df = df.loc[:,df.columns != ind]
if not df.loc[:,df.columns != user].empty:
    print('Nearest neighbors to', user,':\n',df.loc[:,df.columns != user])
    print('The predicted rating:\n',Predictor.prediction(user, df.index.values[1], df2, df))
else:
    print('There is not match user with',user)