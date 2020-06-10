from scipy import spatial
import pandas as pd
import numpy as np
from ratingPrediction import Predictor

array = []
user= 'u'
weights = [0.7, 0.2, 0.1]
def weightedCosine(a, b):
    return 1 - spatial.distance.cosine(a, b, array)

#dataframe with emotions
df = pd.DataFrame([[4, 4, 4], [1, 1, 1], [3, 2, 3], [0, 2, 3],[0, 3, 2], [0, 4, 2]], columns=['u', 'v', 'z'])

for i in range(int(len(df)/3)):
    array = np.concatenate((array, weights))
df2 = pd.DataFrame(df.corr(method=weightedCosine))

print('Ratings of users:\n', df ,'\n')
print('Similarity table:\n', df2 ,'\n')
