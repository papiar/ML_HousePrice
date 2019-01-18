# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:40:07 2019

@author: Pablo
"""

import pandas as pd
import numpy as py


#### Clean data

df = pd.read_csv("test.csv")

#Percentage of null values per column
limit_na = 0.7

#Delete columns with more than limit_na of NA
for col_name in df.columns:
    num_na = df.shape[0] - df[col_name].count()
    #print("For column {} number of NA {}".format(col_name, num_na))
    if num_na > (df.shape[0] * limit_na):
        print("Deleted column {}".format(col_name))
        df = df.drop(columns=[col_name])

#Delete id column
df = df.drop(columns=["Id"])

#Fulfil the na values in the column LotFrontage
list_Neighborhood = df["Neighborhood"].unique()
for aux_col in list_Neighborhood:
    df.loc[(df["LotFrontage"].isna()) & (df["Neighborhood"] == aux_col),"LotFrontage"] = df.loc[(df["Neighborhood"] == aux_col),"LotFrontage"].mean()


#Copiado desde https://www.kaggle.com/caicell/fun-python-eda-step-by-step
nullIndex = df.isnull().any().index[df.isnull().any()]