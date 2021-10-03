import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('./utils/dictionnaire.csv', sep=';')

    ## remove blank line
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    ## normalize data, ie all word in lower()
    df['français'] =  df['français'].apply(lambda x : x.lower())
    df['mahorais'] =  df['mahorais'].apply(lambda x : x.lower())

    return df

    ## get all word french word

    ## get all mahorese word

    ## add translation
