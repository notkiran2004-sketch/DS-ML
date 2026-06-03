import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline

def data_info(df):
    print(df.shape)
    print(df.head(10))
    print("\n Info \n")
    df.info()
    print(df.columns)
    print(df.describe())

def value_info(df):
    print("\n Null Values \n")
    print(df.isnull().sum())
    print("\n Unique Values \n")
    print(df.nunique().sort_values())
    print("\n Duplicates  \n")
    print(df.duplicated().sum())

def seperate_dtypes(df):
    numeric_df = df.select_dtypes(include=['number'])
    categorical_df = df.select_dtypes(include=['object', 'category'])
    return numeric_df, categorical_df

    
    
    