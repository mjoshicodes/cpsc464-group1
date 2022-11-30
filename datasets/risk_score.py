# import os

# import pandas as pd

# from aif360.datasets import StandardDataset



# class RiskDataset(StandardDataset):
#     """German credit Dataset.

#     See :file:`aif360/data/raw/german/README.md`.
#     """
#     def __init__(self, dep_var_name='zfygpa',
#                  protected_attribute_names=['race'],
#                  privileged_classes=[['white']],
#                  instance_weights_name=None,
#                  categorical_features=[],
#                  na_values=[], custom_preprocessing=None,
#                  metadata=None):

#     # def __init__(self, label_name='cost_t', favorable_classes=[1],
#     #              protected_attribute_names=['race'],
#     #              privileged_classes=[['white']],
#     #              instance_weights_name=None,
#     #              categorical_features=['gagne_sum_tm1','gagne_sum_t','our_gagne_score','our_cci_score'],
#     #              features_to_keep=[], features_to_drop=[],
#     #              na_values=[], custom_preprocessing=None,
#     #              metadata=None):

#         # filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#         #                         '..', 'data', 'raw', 'german', 'german.data')

#         filepath = "/Users/megha/Fall_2022/CPSC464/Git/cpsc464-group1/data/data_added.csv"

#         dataset = pd.read_csv(filepath, header=0)
#         X_train,X_test = dataset.get_X(format=pd.DataFrame)
#         y_train, y_test = dataset.get_y(format=pd.Series)
#         A_train, A_test = dataset.get_sensitive_features(name='race',
#                                                          format=pd.Series)
#         all_train = pd.concat([X_train, y_train, A_train], axis=1)
#         all_test = pd.concat([X_test, y_test, A_test], axis=1)
#         df = pd.concat([all_train, all_test], axis=0)

#         # print(filepath)

#         # # filepath = "/IBM_Fairness/AIF360/aif360/data/raw/data_new.csv"
#         # # as given by german.doc
#         # column_names = ['risk_score_t', 'program_enrolled_t', 'cost_t', 'cost_avoidable_t', 'bps_mean_t', 'ghba1c_mean_t', 'hct_mean_t', 'cre_mean_t', 'ldl_mean_t', 'race', 'dem_female', 'dem_age_band_18-24_tm1', 'dem_age_band_25-34_tm1', 'dem_age_band_35-44_tm1', 'dem_age_band_45-54_tm1', 'dem_age_band_55-64_tm1', 'dem_age_band_65-74_tm1', 'dem_age_band_75+_tm1', 'alcohol_elixhauser_tm1', 'anemia_elixhauser_tm1', 'arrhythmia_elixhauser_tm1', 'arthritis_elixhauser_tm1', 'bloodlossanemia_elixhauser_tm1', 'coagulopathy_elixhauser_tm1', 'compdiabetes_elixhauser_tm1', 'depression_elixhauser_tm1', 'drugabuse_elixhauser_tm1', 'electrolytes_elixhauser_tm1', 'hypertension_elixhauser_tm1', 'hypothyroid_elixhauser_tm1', 'liver_elixhauser_tm1', 'neurodegen_elixhauser_tm1', 'obesity_elixhauser_tm1', 'paralysis_elixhauser_tm1', 'psychosis_elixhauser_tm1', 'pulmcirc_elixhauser_tm1', 'pvd_elixhauser_tm1', 'renal_elixhauser_tm1', 'uncompdiabetes_elixhauser_tm1', 'valvulardz_elixhauser_tm1', 'wtloss_elixhauser_tm1', 'cerebrovasculardz_romano_tm1', 'chf_romano_tm1', 'dementia_romano_tm1', 'hemiplegia_romano_tm1', 'hivaids_romano_tm1', 'metastatic_romano_tm1', 'myocardialinfarct_romano_tm1', 'pulmonarydz_romano_tm1', 'tumor_romano_tm1', 'ulcer_romano_tm1', 'cost_dialysis_tm1', 'cost_emergency_tm1', 'cost_home_health_tm1', 'cost_ip_medical_tm1', 'cost_ip_surgical_tm1', 'cost_laboratory_tm1', 'cost_op_primary_care_tm1', 'cost_op_specialists_tm1', 'cost_op_surgery_tm1', 'cost_other_tm1', 'cost_pharmacy_tm1', 'cost_physical_therapy_tm1', 'cost_radiology_tm1', 'lasix_dose_count_tm1', 'lasix_min_daily_dose_tm1', 'lasix_mean_daily_dose_tm1', 'lasix_max_daily_dose_tm1', 'cre_tests_tm1', 'crp_tests_tm1', 'esr_tests_tm1', 'ghba1c_tests_tm1', 'hct_tests_tm1', 'ldl_tests_tm1', 'nt_bnp_tests_tm1', 'sodium_tests_tm1', 'trig_tests_tm1', 'cre_min-low_tm1', 'cre_min-high_tm1', 'cre_min-normal_tm1', 'cre_mean-low_tm1', 'cre_mean-high_tm1', 'cre_mean-normal_tm1', 'cre_max-low_tm1', 'cre_max-high_tm1', 'cre_max-normal_tm1', 'crp_min-low_tm1', 'crp_min-high_tm1', 'crp_min-normal_tm1', 'crp_mean-low_tm1', 'crp_mean-high_tm1', 'crp_mean-normal_tm1', 'crp_max-low_tm1', 'crp_max-high_tm1', 'crp_max-normal_tm1', 'esr_min-low_tm1', 'esr_min-high_tm1', 'esr_min-normal_tm1', 'esr_mean-low_tm1', 'esr_mean-high_tm1', 'esr_mean-normal_tm1', 'esr_max-low_tm1', 'esr_max-high_tm1', 'esr_max-normal_tm1', 'ghba1c_min-low_tm1', 'ghba1c_min-high_tm1', 'ghba1c_min-normal_tm1', 'ghba1c_mean-low_tm1', 'ghba1c_mean-high_tm1', 'ghba1c_mean-normal_tm1', 'ghba1c_max-low_tm1', 'ghba1c_max-high_tm1', 'ghba1c_max-normal_tm1', 'hct_min-low_tm1', 'hct_min-high_tm1', 'hct_min-normal_tm1', 'hct_mean-low_tm1', 'hct_mean-high_tm1', 'hct_mean-normal_tm1', 'hct_max-low_tm1', 'hct_max-high_tm1', 'hct_max-normal_tm1', 'ldl_min-low_tm1', 'ldl_min-high_tm1', 'ldl_min-normal_tm1', 'ldl-mean-low_tm1', 'ldl-mean-high_tm1', 'ldl-mean-normal_tm1', 'ldl_max-low_tm1', 'ldl_max-high_tm1', 'ldl_max-normal_tm1', 'nt_bnp_min-low_tm1', 'nt_bnp_min-high_tm1', 'nt_bnp_min-normal_tm1', 'nt_bnp_mean-low_tm1', 'nt_bnp_mean-high_tm1', 'nt_bnp_mean-normal_tm1', 'nt_bnp_max-low_tm1', 'nt_bnp_max-high_tm1', 'nt_bnp_max-normal_tm1', 'sodium_min-low_tm1', 'sodium_min-high_tm1', 'sodium_min-normal_tm1', 'sodium_mean-low_tm1', 'sodium_mean-high_tm1', 'sodium_mean-normal_tm1', 'sodium_max-low_tm1', 'sodium_max-high_tm1', 'sodium_max-normal_tm1', 'trig_min-low_tm1', 'trig_min-high_tm1', 'trig_min-normal_tm1', 'trig_mean-low_tm1', 'trig_mean-high_tm1', 'trig_mean-normal_tm1', 'trig_max-low_tm1', 'trig_max-high_tm1', 'trig_max-normal_tm1', 'gagne_sum_tm1', 'gagne_sum_t']
#         # try:
#         #     df = pd.read_csv(filepath, header=0)
#         #     # print("This RAN")
#         #     # print(df.shape[0])
#         #     # # print( df.columns.tolist())
#         #     # keep = (set(features_to_keep) | set(protected_attribute_names)
#         #     #   | set(categorical_features) | set([label_name]))
#         #     # print(keep)
#         #     # df = df[sorted(keep - set(features_to_drop), key=df.columns.get_loc)]
#         #     # print(df.columns.get_loc)
#         # except IOError as err:
#         #     pass
#         #     # print("IOError: {}".format(err))
#         #     # print("To use this class, please download the following files:")
#         #     # print("\n\thttps://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data")
#         #     # print("\thttps://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.doc")
#         #     # print("\nand place them, as-is, in the folder:")
#         #     # print("\n\t{}\n".format(os.path.abspath(os.path.join(
#         #     #     os.path.abspath(__file__), '..', '..', 'data', 'raw', 'german'))))
#         #     # import sys
#         #     # sys.exit(1)

#         super(RiskDataset, self).__init__(df=df,
#             dep_var_name=dep_var_name,
#             protected_attribute_names=protected_attribute_names,
#             privileged_classes=privileged_classes,
#             instance_weights_name=instance_weights_name,
#             categorical_features=categorical_features,
#             na_values=na_values,
#             custom_preprocessing=custom_preprocessing, metadata=metadata)

#         # super(RiskDataset, self).__init__(df=df, label_name=label_name,
#         #     favorable_classes=favorable_classes,
#         #     protected_attribute_names=protected_attribute_names,
#         #     privileged_classes=privileged_classes,
#         #     instance_weights_name=instance_weights_name,
#         #     categorical_features=categorical_features,
#         #     features_to_keep=features_to_keep,
#         #     features_to_drop=features_to_drop, na_values=na_values,
#         #     custom_preprocessing=custom_preprocessing, metadata=metadata)
#         # # print(df)
#         # # print(df['bps_mean_t'])
    
# # if __name__ == "__main__":
# #     object_test = RiskDataset()


# # import os

# # import pandas as pd

# # from aif360.datasets import StandardDataset

# # default_mappings = {
# #     'label_maps': [{1.0: '>= 10 Visits', 0.0: '< 10 Visits'}],
# #     'protected_attribute_maps': [{1.0: 'White', 0.0: 'Non-White'}]
# # }

# # def default_preprocessing(df):
# #     """
# #     1.Create a new column, RACE that is 'White' if RACEV2X = 1 and HISPANX = 2 i.e. non Hispanic White
# #       and 'non-White' otherwise
# #     2. Restrict to Panel 19
# #     3. RENAME all columns that are PANEL/ROUND SPECIFIC
# #     4. Drop rows based on certain values of individual features that correspond to missing/unknown - generally < -1
# #     5. Compute UTILIZATION, binarize it to 0 (< 10) and 1 (>= 10)
# #     """
# #     def race(row):
# #         if ((row['race'] == 1)):  #non-Hispanic Whites are marked as WHITE; all others as NON-WHITE
# #             return 'White'
# #         return 'Non-White'

# #     df['race'] = df.apply(lambda row: race(row), axis=1)

# #     return df


# # class RiskDataset(StandardDataset):

# #     def __init__(self, label_name='our_cci_score', favorable_classes=[1.0],
# #                  protected_attribute_names=['race'],
# #                  privileged_classes=[['Non-White']],
# #                  instance_weights_name=None,
# #                  categorical_features=['trig_min-low_tm1', 'trig_min-high_tm1', 'trig_min-normal_tm1', 'trig_mean-low_tm1', 'trig_mean-high_tm1', 'trig_mean-normal_tm1', 'trig_max-low_tm1', 'trig_max-high_tm1', 'trig_max-normal_tm1', 'gagne_sum_tm1', 'gagne_sum_t', 'our_gagne_score'],
# #                  features_to_keep=['trig_min-low_tm1', 'trig_min-high_tm1', 'trig_min-normal_tm1', 'trig_mean-low_tm1', 'trig_mean-high_tm1', 'trig_mean-normal_tm1', 'trig_max-low_tm1', 'trig_max-high_tm1', 'trig_max-normal_tm1', 'gagne_sum_tm1', 'gagne_sum_t', 'our_gagne_score', 'our_cci_score'],
# #                  features_to_drop=[],
# #                  na_values=[], custom_preprocessing=default_preprocessing,
# #                  metadata=default_mappings):

# #         filepath = "/Users/megha/Fall_2022/CPSC464/Git/cpsc464-group1/data/data_added.csv"

# #         try:
# #             df = pd.read_csv(filepath, sep=',', na_values=na_values, index_col=0)
# #         except IOError as err:
# #             print("IOError: {}".format(err))
# #             print("To use this class, please follow the instructions in:")
# #             print("\n\t{}\n".format(os.path.abspath(os.path.join(
# #                os.path.abspath(__file__), '..', '..', 'data', 'raw', 'meps', 'README.md'))))
# #             print("\n to download and convert the 2015 data and place the final h181.csv file, as-is, in the folder:")
# #             print("\n\t{}\n".format(os.path.abspath(os.path.join(
# #                os.path.abspath(__file__), '..', '..', 'data', 'raw', 'meps'))))
# #             import sys
# #             sys.exit(1)

# #         super(RiskDataset, self).__init__(df=df, label_name=label_name,
# #             favorable_classes=favorable_classes,
# #             protected_attribute_names=protected_attribute_names,
# #             privileged_classes=privileged_classes,
# #             instance_weights_name=instance_weights_name,
# #             categorical_features=categorical_features,
# #             features_to_keep=features_to_keep,
# #             features_to_drop=features_to_drop, na_values=na_values,
# #             custom_preprocessing=custom_preprocessing, metadata=metadata)


import os

import pandas as pd

from aif360.datasets import StandardDataset

default_mappings = {
    'protected_attribute_maps': [{1.0: 'white', 0.0: 'black'}]
}


class RiskDataset(StandardDataset):
    """Risk score Dataset.

    See :file:`aif360/data/raw/meps/README.md`.
    """

    def __init__(self, label_name='our_cci_score', favorable_classes=[1.0],
                 protected_attribute_names=['race'],
                 privileged_classes=[['white']],
                 instance_weights_name=None,
                 categorical_features=['trig_min-low_tm1', 'trig_min-high_tm1', 'trig_min-normal_tm1', 'trig_mean-low_tm1', 'trig_mean-high_tm1', 'trig_mean-normal_tm1', 'trig_max-low_tm1', 'trig_max-high_tm1', 'trig_max-normal_tm1', 'gagne_sum_tm1', 'gagne_sum_t', 'our_gagne_score'],
                 features_to_keep=['trig_min-low_tm1', 'trig_min-high_tm1', 'trig_min-normal_tm1', 'trig_mean-low_tm1', 'trig_mean-high_tm1', 'trig_mean-normal_tm1', 'trig_max-low_tm1', 'trig_max-high_tm1', 'trig_max-normal_tm1', 'gagne_sum_tm1', 'gagne_sum_t', 'our_gagne_score'],
                 features_to_drop=[],
                 na_values=[],
                 metadata=default_mappings):

        filepath = "/Users/megha/Fall_2022/CPSC464/Git/cpsc464-group1/data/data_added.csv"

        try:
            df = pd.read_csv(filepath, sep=',', na_values=na_values, index_col=0)
            df['instace_weights'] = 1.0
        except IOError as err:
            print("IOError: {}".format(err))
            print("To use this class, please follow the instructions in:")
            print("\n\t{}\n".format(os.path.abspath(os.path.join(
               os.path.abspath(__file__), '..', '..', 'data', 'raw', 'meps', 'README.md'))))
            print("\n to download and convert the 2015 data and place the final h181.csv file, as-is, in the folder:")
            print("\n\t{}\n".format(os.path.abspath(os.path.join(
               os.path.abspath(__file__), '..', '..', 'data', 'raw', 'meps'))))
            import sys
            sys.exit(1)

        super(RiskDataset, self).__init__(df=df, label_name=label_name,
            favorable_classes=favorable_classes,
            protected_attribute_names=protected_attribute_names,
            privileged_classes=privileged_classes,
            instance_weights_name=instance_weights_name,
            categorical_features=categorical_features,
            features_to_keep=features_to_keep,
            features_to_drop=features_to_drop, na_values=na_values, metadata=metadata)
