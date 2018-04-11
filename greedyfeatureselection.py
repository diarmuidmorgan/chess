#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

#Load in the updated data file from homework 1

df = df = pd.read_csv('diarmuid-cleaned-1.csv',  keep_default_na=True, sep=',\s+', delimiter=',', skipinitialspace=True)

#drop the mysterious 'unamed: 0' column and the redundant 'customer' column
df = df.drop('Unnamed: 0', 1)
df = df.drop('Unnamed: 0.1', 1)
df = df.drop('customer', 1)

df.describe().T
df['income']=df['income'].astype('category')
df['churn']=df['churn'].astype('int64')
categorical_columns = df[['regionType','marriageStatus','income','creditRating', 'creditCard', 'children', 'homeOwner']].columns
msk = np.random.rand(len(df)) < 0.7

df_train = df[msk]

df_test = df[~msk]
X = df_train
Y=df_train.churn
features = df.columns


from math import inf
import statsmodels.formula.api as sm
best = inf
best_feature_string=''
def greedyfeatureselection(features, usedFeatures, featureString):

    global best
    global best_feature_string
    global df_train
    global df_test
    for feature in features:
        f=feature

        if feature not in usedFeatures:
            if feature in categorical_columns:
                feature = 'C('+feature+')'

            if featureString[-1] == '~':
                new_feature_string = featureString+' '+feature
            else:
                new_feature_string = featureString+' + '+feature

            model = sm.ols(formula=new_feature_string, data=df_train).fit()

            mse = ((df_test.churn - model.predict(df_test))** 2).mean()

            del(model)
            if mse<best:
                best = mse
                best_feature_string=new_feature_string
                f=open('results.txt', 'a')
                f.write(str(best)+' '+best_feature_string)
                print('New best:'', best)
                print(best_feature_string)
                f.close()


            print('\n\n')
            if len(usedFeatures)<len(features):
                new_used_features = usedFeatures + [f]
                greedyfeatureselection(features, new_used_features, new_feature_string)


greedyfeatureselection(features, [], 'churn ~')
print('done')
print(best)
print(best_feature_string)
