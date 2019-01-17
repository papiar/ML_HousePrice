# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:40:07 2019

@author: Pablo
"""

import pandas as pd
import numpy as py


#### Clean data

df = pd.read_csv("test.csv")


df.shape[1]

#Delete columns with more than 70% of NA
for col_name in df.columns:
    num_na = df.shape[0] - df[col_name].count()
    #print("For column {} number of NA {}".format(col_name, num_na))
    if num_na > (df.shape[0] * 0.7):
        print("Deleted column {}".format(col_name))
        df = df.drop(columns=[col_name])

