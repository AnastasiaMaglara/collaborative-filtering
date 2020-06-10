import numpy as np

class Predictor:
    def prediction(u, i, sim, df):
        sum = 0
        div = 0
        for v in df.loc[i,:].index:
            if df.loc[i, v]!=0:
                df = df.replace(0, np.NaN)
                mean = df[v].mean()
                df = df.replace(np.NaN, 0)
                sum = sum + sim[u][v] * (df.loc[i,v]-mean)
                div = div + sim[u][v]
        df = df.replace(0, np.NaN)
        sum = sum/div + df[u].mean()
        df = df.replace(np.NaN, 0)
        return round(sum, 6)