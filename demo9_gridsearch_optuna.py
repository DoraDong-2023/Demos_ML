# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:09:14 2022

@author: Admin
"""

import optuna
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, train_test_split
import optuna
from optuna.samplers import TPESampler        
import sklearn.neural_network
from sklearn.metrics import roc_auc_score
from optuna.pruners import MedianPruner



N = 100
num_features = 5
X, y = np.random.randn(N,num_features), np.round(np.random.rand(N,1))
X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.2)


from sklearn.neural_network import MLPClassifier

mlp_clf = MLPClassifier(alpha=3.5, hidden_layer_sizes=150,random_state = 42)
mlp_clf.fit(X_train, y_train)
mlp_prediction_proba = mlp_clf.predict_proba(X_test)[:, 1]
roc_auc_score(y_test,mlp_prediction_proba)
print(roc_auc_score(y_test,mlp_prediction_proba))


# Cross Valid 5
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

cv_scores=[]
for idx, (train_idx, test_idx) in enumerate(cv.split(X, y)):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
        
    model = sklearn.neural_network.MLPClassifier(alpha=3.5, hidden_layer_sizes=150, random_state=42)
    model.fit(
            X_train,
            y_train)
        
    test_proba = model.predict_proba(X_test)
    cv_scores.append(roc_auc_score(y_test,test_proba[:,1]))
print(np.mean(cv_scores))


def objective(trial):
    param= {# the params need to train
        "alpha": trial.suggest_float("alpha", 1, 5, step=0.1),       
        "learning_rate_init" : trial.suggest_loguniform('learning_rate_init', 1e-5, 1e-2),
        "hidden_layer_sizes" : trial.suggest_int('hidden_layer_sizes', 150, 500,step=50)
}
    
    cv_scores = []
    
    for idx, (train_idx, test_idx) in enumerate(cv.split(X, y)):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        
        model = sklearn.neural_network.MLPClassifier(random_state=42, max_iter=1000, **param)
        model.fit(
            X_train,
            y_train)        
        
        test_proba = model.predict_proba(X_test)
        cv_scores.append(roc_auc_score(y_test,test_proba[:,1]))
    return np.mean(cv_scores)# define the desired optimal metrics

study = optuna.create_study(sampler=TPESampler(seed=42), pruner = MedianPruner(), direction="maximize")
study.optimize(objective, n_trials=100, n_jobs=-1) 
     
print("Best trial:", study.best_trial)










