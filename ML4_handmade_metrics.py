#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[83]:


def confusion_matrix(y_true, y_pred):
    
    tp = sum((y_true == 1) & (y_pred == 1))
    tn = sum((y_true == 0) & (y_pred == 0))
    fn = sum((y_true == 1) & (y_pred == 0))
    fp = sum((y_true == 0) & (y_pred == 1))
    return tp,tn,fn,fp
def precision(tp,tn,fn,fp):
    return (tp  )/ (float( tp + fp))
def recall(tp,tn,fn,fp):
    return (tp  )/ float( tp + fn)
def f1_score(tp,tn,fn,fp):
    prec = precision(tp,tn,fn,fp)
    reca = recall(tp,tn,fn,fp)
    f1_score = (2*prec*reca)/ (prec + reca)
    return f1_score
def accuracy(tp,tn,fn,fp):
    return ((tp + tn) )/ ( tp + tn + fn + fp)


# In[33]:





# In[87]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




