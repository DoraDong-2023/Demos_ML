#!/usr/bin/env python
# coding: utf-8

# # load data
# data enhancement
# ML classification task

get_ipython().system('pip install xgboost catboost lightgbm imbearn')


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from sklearn.metrics import accuracy_score, roc_auc_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.naive_bayes import GaussianNB

from imblearn.over_sampling import RandomOverSampler  
from imblearn.over_sampling import SMOTE  
from imblearn.over_sampling import BorderlineSMOTE  
from imblearn.over_sampling import ADASYN  


from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.utils import shuffle


PATH_TO_DATASET = './Churn_Modelling.csv' 

seed = 16#0, 8, 16, 24, 32 and take average

data = pd.read_csv(PATH_TO_DATASET)
data.head()

print(data.info())


# # preprocessing

# In[ ]:


cats = data.select_dtypes(include=['object','bool'])#categorical
print(cats)

# if exists nan, interpolate for numerical value
data = data.interpolate()
# if exists nan, interpolate for object value
data.fillna(method ='ffill', inplace = True)
data.fillna(method ='backfill', inplace = True)

# categorical to values
from sklearn.preprocessing import LabelEncoder#categorical
list_label_encoder = []
for name in list(cats):
    list_label_encoder.append(LabelEncoder())
    data[name] = list_label_encoder[-1].fit_transform(data[name])

for name in list_label_encoder:
    print(name.classes_)


# In[ ]:


# print the score
def print_score(model,X_train,y_train,X_test,y_test):
    print('training score is : ', model.score(X_train, y_train))
    print('test score is : ', model.score(X_test, y_test))
    print('training auc is : ', roc_auc_score(model.predict(X_train), y_train))
    print('test auc is : ', roc_auc_score(model.predict(X_test), y_test))


# # standardlization

# In[ ]:


X = data.to_numpy()[:,:-1]
y = data.to_numpy()[:,-1]
scaler = preprocessing.StandardScaler().fit(X)
X = scaler.fit_transform(X)


# In[ ]:


# split
type_data_dict = {'1':'normal', '2':'semi-supervised','3':'RandomOverSampler',
                 '4':'SMOTE','5':'BorderlineSMOTE','6':'ADASYN'}
type_data = '1'
if type_data=='1':
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=seed, stratify=y)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train,test_size = 0.133, random_state=seed, stratify=y_train)
elif type_data=='2':
    # semi-supervised
    X, y = shuffle(X, y, random_state=seed)
    X_train = X[:50]
    y_train = y[:50]
    X_test = X[50:]
    y_test = y[50:]
elif type_data=='3':
    # oversampling
    # here only test for supervised, RandomOverSampler
    ros = RandomOverSampler(random_state=0)
    X_train, y_train = ros.fit_resample(X, y)
elif type_data=='4':
    smo = SMOTE(random_state=42)
    X_train, y_train = smo.fit_resample(X, y)
elif type_data=='5':
    bsmo = BorderlineSMOTE(kind='borderline-1',random_state=42) #kind='borderline-2'
    X_train, y_train = bsmo.fit_resample(X, y)
elif type_data=='6':
    ana = ADASYN(random_state=0)
    X_train, y_train = ana.fit_resample(X, y)


# # build model

# In[ ]:


# build model

model_list = [KNeighborsClassifier(n_neighbors=2),
              LogisticRegression(),
             RandomForestClassifier(),
             MLPClassifier(max_iter=100, solver='sgd',activation = 'identity', hidden_layer_sizes = (100,50)),
             SVC(),
             XGBClassifier(),
             CatBoostClassifier(n_estimators=100),
             LGBMClassifier(),
             GaussianNB(),
              LabelPropagation(max_iter=100,kernel='rbf',gamma=0.1),
              LabelSpreading(max_iter=100,kernel='rbf',gamma=0.1)
             ]
for model in model_list:
    model.fit(X_train,y_train)
    print_score(model,X_train,y_train,X_test,y_test)


# In[ ]:





# In[ ]:





# In[ ]:




