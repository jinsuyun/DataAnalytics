import numpy as np
from matplotlib import pyplot as plt
import pandas as pd



def read_dataset():
    return pd.read_csv('../iris.csv'), pd.read_csv('../iris_metadata.csv')

def merge_dfs(iris, metadata):
    ### complete here
    return pd.merge(iris,metadata,left_on='species',right_on='name')

def split_df(df, ratio):
    ### complete here
    splited_index=round(len(df) * ratio)

    return df.iloc[:splited_index],df.iloc[splited_index:] #iloc는 integer position을 통해 값을 찾을 수 있다.
#예를 들어 [:3]이라 하면 1~3번째 row까지
def truncate_non_toxics(df):
    ### complete here

    return df.loc[df['toxic']>0] # loc는 label을 통해 값을 찾을 수 있다.
#예를 들어 [:3]이라 하면 첫번째 row부터 이름이 '3'인 row까지

def main():
    split_ratio = 0.7
    iris, metadata = read_dataset()
    ### complete here

    merge_data=merge_dfs(iris,metadata)
    split_data=split_df(merge_data,split_ratio)

    training_data=truncate_non_toxics(split_data[0])
    test_data=truncate_non_toxics(split_data[1])

    print(training_data.describe())
    print()
    print(test_data.describe())

main()


