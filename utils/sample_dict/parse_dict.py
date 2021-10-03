import numpy as np
import pandas as pd

df = pd.read_csv('./dictionnaire.csv', sep=';')
print(df)

## remove blank line
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)

## normalize data, ie all word in lower()
df['français'] =  df['français'].apply(lambda x : x.lower())
df['mahorais'] =  df['mahorais'].apply(lambda x : x.lower())
print(df)

## get all word french word

## get all mahorese word

## add translation
