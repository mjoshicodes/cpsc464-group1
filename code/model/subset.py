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
    data_fp = os.path.join(git_dir, 'data', 'data_new.csv')

    # load df
    data_df = pd.read_csv(data_fp)

    # because we removed patient
    data_df = data_df.reset_index()
    return data_df

def create_new_df(df):
    new_df = df.copy()
    indices_zero_gagne = []

    for index, row in new_df.iterrows():
        if row['gagne_sum_t'] == 0:
            indices_zero_gagne.append(index)
    #print(indices_zero_gagne)
    new_df = new_df.drop(indices_zero_gagne)
    return new_df


def generate_stats(df):
    race_white = 0
    sum_gagne_white = 0
    gagne_zero_white = 0

    race_black = 0
    gagne_zero_black = 0
    sum_gagne_black = 0
    for index, row in df.iterrows():
        if row['race'] == 'white':
            race_white += 1

            if row['gagne_sum_t'] != 0:
                sum_gagne_white += row['gagne_sum_t']

            else:
                gagne_zero_white += 1
            
        else:
            
            race_black += 1
            if row['gagne_sum_t'] != 0:
                sum_gagne_black += row['gagne_sum_t']

            else:
                gagne_zero_black += 1



    print("# BLACK: " + str(race_black) + " GAGNE AVG: " + str(float(sum_gagne_black) / race_black))
    print('Black with zero gagne: ' + str(gagne_zero_black))
    print('# WHITE: ' + str(race_white) + " GAGNE AVG: " + str(float(sum_gagne_white) / race_white))
    print('White with zero gagne: ' + str(gagne_zero_white))

def main():
    # load data
    data_df = load_data_df()
    print("PRELIMINARY STATS")
    generate_stats(data_df)

    dropped_df = create_new_df(data_df)
    print("NEW STATS")
    generate_stats(dropped_df)


if __name__ == '__main__':
    main()
