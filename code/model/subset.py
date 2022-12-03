"""
Main script to train lasso model and save predictions.
"""
import pandas as pd
import numpy as np
import os

import features
import model
import util

def load_data_df():
    """Load data dataframe.

    Returns
    -------
    pd.DataFrame
        DataFrame to use for analysis.

    """
    # define filepath
    git_dir = util.get_git_dir()
    data_fp = os.path.join(git_dir, 'data', 'data_added.csv')

    # load df
    data_df = pd.read_csv(data_fp)

    # because we removed patient
    data_df = data_df.reset_index()
    return data_df

def create_new_df(df):
    gagne_variable = 'tumor_romano_tm1'
    #gagne_list = ['metastatic_romano_tm1', 'chf_romano_tm1', 'dementia_romano_tm1', 'renal_elixhauser_tm1', 'wtloss_elixhauser_tm1']
    new_df = df.copy()
    indices_zero_gagne = []

    for index, row in new_df.iterrows():
        if row[gagne_variable] <= 0:
            indices_zero_gagne.append(index)

    new_df = new_df.drop(indices_zero_gagne)
    return new_df

def generate_stats(df):
    black_patients = 0
    white_patients = 0

    sum_gagne_white = 0
    white_subset = 0

    sum_gagne_black = 0
    black_subset = 0
    gagne_variable = 'tumor_romano_tm1'
    for index, row in df.iterrows():
        if row['race'] == 'white':
            white_patients += 1
            if row[gagne_variable] <= 0:
                white_subset += 1
            sum_gagne_white += row[gagne_variable]
            
        else:
            black_patients += 1
            if row[gagne_variable] <= 0:
                black_subset += 1
            sum_gagne_black += row[gagne_variable]

    print("# BLACK: " + str(black_patients) + " GAGNE AVG: " + str(float(sum_gagne_black) / black_patients))
    print('Black removed from subset: ' + str(black_subset))
    print('# WHITE: ' + str(white_patients) + " GAGNE AVG: " + str(float(sum_gagne_white) / white_patients))
    print('White removed from subset: ' + str(white_subset))


def main():
    # load data
    data_df = load_data_df()
    print("PRELIMINARY STATS")
    generate_stats(data_df)

    dropped_df = create_new_df(data_df)
    print("NEW STATS")
    generate_stats(dropped_df)
    dropped_df.to_csv("../../data/data_subsetted.csv")


if __name__ == '__main__':
    main()
