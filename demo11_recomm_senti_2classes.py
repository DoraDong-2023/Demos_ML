#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_distances
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


# Recommendations
# 1. TF-IDF
# 2. LDA
# Sentiment Analysis
# 1. TF-IDF
# 2. classification on 2 classes

#####
file_path1='./data/jcpenney-products_subset.csv.zip'
file_path2='./data/amazon-petsupply-reviews_subset.csv.zip'
keyword1='description'
keyword2='rating'
###########

# The dataset
if file_path1.endswith('.zip'):
    df_data1=pd.read_csv(file_path1, compression='infer')
else:
    df_data1 = pd.read_csv(file_path1)

tfidf = TfidfVectorizer(ngram_range=(1, 2), min_df=5, max_df=.2)
X_tfidf = tfidf.fit_transform(df_data1[keyword1])
tfidf.inverse_transform(X_tfidf[0])

vocab = tfidf.get_feature_names()
vocab = [vocabi.replace(' ','_') for vocabi in vocab]
vocab = np.array(vocab)


# LDA
lda = LatentDirichletAllocation(n_components=20, n_jobs=-1, random_state=123)
X_lda = lda.fit_transform(X_tfidf)

theta_0 = np.round(X_lda[0],2)
print(f'theta_9: {theta_0 :}\n')
n_assigned_0=(theta_0>0.01).sum()
print(f'n_assigned_0:{n_assigned_0 :}\n')
assigned_topics_0 = np.argsort(theta_0)[::-1][:1]
print(f'assigned_topics_0:{assigned_topics_0 :}')

per_topic_term_dis = lda.components_
topic_idx = []
for topic_idx in range(len(per_topic_term_dis)):
    topic = per_topic_term_dis[topic_idx, :]
    temp_index = np.argsort(topic)[::-1]
    content = ' '.join([vocab[i] for i in temp_index[:5]])
    #print(f'Topic #{topic_idx:2d} : ', content)

# Generate Similarity Matrix
distances = cosine_distances(X_lda)
df_data1.name_title[np.argsort(distances[0])[:10]].values

# dataset2
if file_path2.endswith('.zip'):
    df_data2=pd.read_csv(file_path2, compression='infer')
else:
    df_data2 = pd.read_csv(file_path2)
y = df_data2[keyword2]==5

reviews_train,reviews_test,y_train,y_test = train_test_split(df_data2.review, y, train_size = .2, stratify=y)

# TF-IDF+GBC
pipe_gbc = Pipeline([('tfidf', TfidfVectorizer(min_df=5, max_df=.5)), ('gbc', GradientBoostingClassifier(n_estimators=200))])

# grid search
param_grid = {'tfidf__ngram_range':[(1, 2), (1,1)], 'gbc__max_depth':[2,10], }
gs_pipe_gbc = GridSearchCV(pipe_gbc, param_grid, cv=2, n_jobs=-1).fit(reviews_train,y_train)
# print best parameters, predict
print(gs_pipe_gbc.best_params_, gs_pipe_gbc.best_score_, gs_pipe_gbc.score(reviews_test,y_test))
gs_pipe_gbc.predict(['Good.','AAAA'])




