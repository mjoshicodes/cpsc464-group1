"""
Main script to train add new index variables.
"""
import pandas as pd
import numpy as np
import os

def load_data_df():
    """Load data dataframe.

    Returns
    -------
    pd.DataFrame
        DataFrame to use for analysis.

    """
    # define filepath
    data_fp = 'data_new.csv'

    # load df
    data_df = pd.read_csv(data_fp)
    return data_df

def create_our_gagne_col(df):
    new_col = 5 * df["metastatic_romano_tm1"] + 2 * df["chf_romano_tm1"] + 2 * df["dementia_romano_tm1"] + 2 * df["renal_elixhauser_tm1"] + 2 * df["wtloss_elixhauser_tm1"] + df["hemiplegia_romano_tm1"] + df["alcohol_elixhauser_tm1"] + df["tumor_romano_tm1"] + df["arrhythmia_elixhauser_tm1"] + df["pulmonarydz_romano_tm1"] + df["coagulopathy_elixhauser_tm1"] + df["compdiabetes_elixhauser_tm1"] + df["anemia_elixhauser_tm1"] + df["electrolytes_elixhauser_tm1"] + df["liver_elixhauser_tm1"] + df["pvd_elixhauser_tm1"] + df["psychosis_elixhauser_tm1"] + df["pulmcirc_elixhauser_tm1"] - df["hivaids_romano_tm1"] - df["hypertension_elixhauser_tm1"]
    #new_col = df["bps_mean_t"]
    return new_col

def main():
    df = load_data_df()
    df["our_gagne_score"] = create_our_gagne_col(df)
    df.to_csv("data_added.csv")

if __name__ == '__main__':
    main()