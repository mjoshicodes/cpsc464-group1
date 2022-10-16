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

def create_dropped_cost_df(df):
    df.drop(columns=['cost_dialysis_tm1', 'cost_emergency_tm1', 'cost_home_health_tm1', 'cost_ip_medical_tm1', 'cost_ip_surgical_tm1', 'cost_laboratory_tm1', 'cost_op_primary_care_tm1', 'cost_op_specialists_tm1', 'cost_op_surgery_tm1', 'cost_other_tm1', 'cost_pharmacy_tm1', 'cost_physical_therapy_tm1', 'cost_radiology_tm1'])
    return df

def main():
    df = load_data_df()
    df["our_gagne_score"] = create_our_gagne_col(df)
    df.to_csv("data_added.csv")

    # Removing cost data
    # df = load_data_df()
    # df.drop(['cost_dialysis_tm1', 'cost_emergency_tm1', 'cost_home_health_tm1', 'cost_ip_medical_tm1', 'cost_ip_surgical_tm1', 'cost_laboratory_tm1', 'cost_op_primary_care_tm1', 'cost_op_specialists_tm1', 'cost_op_surgery_tm1', 'cost_other_tm1', 'cost_pharmacy_tm1', 'cost_physical_therapy_tm1', 'cost_radiology_tm1'], axis=1, inplace=True)
    # df["our_gagne_score"] = create_our_gagne_col(df)
    # df.to_csv("data_removed_cost.csv")

if __name__ == '__main__':
    main()