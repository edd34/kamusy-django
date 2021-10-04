import numpy as np
import pandas as pd

def get_dict_mahorais():
    df = pd.read_csv('./utils/dictionnaire.csv', sep=';')

    ## remove blank line
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    ## normalize data, ie all word in lower()
    df['français'] =  df['français'].apply(lambda x : x.lower())
    df['mahorais'] =  df['mahorais'].apply(lambda x : x.lower())
    return df

def get_dict_kibushi():
    df = pd.read_csv('./utils/dictionnaire-kibushi.csv', sep=';')

    ## remove blank line
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    ## normalize data, ie all word in lower()
    df['français'] =  df['français'].apply(lambda x : x.lower())
    df['kibushi'] =  df['kibushi'].apply(lambda x : x.lower())

    return df