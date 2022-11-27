
# a demo for several metrics api
import numpy as np
from sklearn import datasets

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import *

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

#
def make_data(centers=3, cluster_std=[1.0, 3.0, 2.5], n_samples=150, n_features=2):
    X, y = make_blobs(n_samples, n_features)
    return X, y

def sensitivity(y_test, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    return tp/(tp+fn)
def specificity(y_test, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    return tn / (tn+fp)

def bootstrap_metris(clf, X_train, y_train, X_test, y_test, metrics='auc', inter_per = 95, nsamples=1000):
    values = []
    for b in tqdm(range(nsamples)):
        idx = np.random.randint(X_train.shape[0], size=X_train.shape[0])
        clf.fit(X_train[idx], y_train[idx])
        pred = clf.predict_proba(X_test)[:, 1]
        if metrics=='auc':
            value = roc_auc_score(y_test.ravel(), pred.ravel())
        elif metrics=='specifcity':
            value = specificity(y_test.ravel(), clf.predict(X_test).ravel())
        elif metrics=='sensitivity':
            value = sensitivity(y_test.ravel(), clf.predict(X_test).ravel())
        elif metrics=='balanced':
            value = balanced_accuracy_score(y_test.ravel(), clf.predict(X_test).ravel())
        elif metrics=='f1_score':
            value = f1_score(y_test.ravel(), clf.predict(X_test).ravel())
        values.append(value)
    return np.percentile(values, ((100-inter_per)/2, (100+inter_per)/2))
def main():
    # data
    data = load_breast_cancer()
    X = data['data']
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    
    # model
    lr_l1 = LogisticRegression(penalty="l1", C=0.5, solver="liblinear")
    lr_l1.fit(X_train, y_train)
    # pred
    y_pred = lr_l1.predict(X_test)
    y_pred_score = lr_l1.predict_proba(X_test)
    
    iter=1000
    inter_pre=95

    # metrics
    print('f1 score : ',f1_score(y_test, y_pred),'(',bootstrap_metris(lr_l1, X_train, y_train, X_test, y_test,'auc',inter_pre,iter),')')
    
    print('balanced accuracy : ',balanced_accuracy_score(y_test, y_pred),'(',bootstrap_metris(lr_l1, X_train, y_train, X_test, y_test,'specifcity',inter_pre,iter),')')
    
    print('sensitivity : ',sensitivity(y_test, y_pred),'(',bootstrap_metris(lr_l1, X_train, y_train, X_test, y_test,'sensitivity',inter_pre,iter),')')
    
    print('specifcity : ',specificity(y_test, y_pred),'(',bootstrap_metris(lr_l1, X_train, y_train, X_test, y_test,'balanced',inter_pre,iter),')')
    
    print('auc : ',roc_auc_score(y_test, y_pred_score[:,1]),'(',bootstrap_metris(lr_l1, X_train, y_train, X_test, y_test,'f1_score',inter_pre,iter),')')


main()




"""
# clustering metrics
metrics.adjusted_mutual_info_score(…[, …])
metrics.adjusted_rand_score(labels_true, …)
metrics.calinski_harabasz_score(X, labels)
metrics.davies_bouldin_score(X, labels)
metrics.completeness_score(labels_true, …)
metrics.cluster.contingency_matrix(…[, …])
metrics.fowlkes_mallows_score(labels_true, …)
metrics.homogeneity_completeness_v_measure(…)
metrics.homogeneity_score(labels_true, …)
metrics.mutual_info_score(labels_true, …)
metrics.normalized_mutual_info_score(…[, …])
metrics.silhouette_score(X, labels[, …])
metrics.silhouette_samples(X, labels[, metric])
metrics.v_measure_score(labels_true, labels_pred)
"""
