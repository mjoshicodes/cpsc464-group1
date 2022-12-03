"""
Build Table 2: performance of predictors trained on alternative labels.
"""
import pandas as pd
import os
import model.util as util


def get_concentration_metric_df(k, holdout_pred_df,
                                y_predictors=['log_cost_t',
                                              'log_cost_avoidable_t',
                                              'gagne_sum_t',
                                              'our_gagne_score'],
                                outcomes=['log_cost_t', 'log_cost_avoidable_t',
                                          'gagne_sum_t', 'our_gagne_score', 'dem_race_black']):
    """Calculate concentration of a given outcome of interest (columns) for
    each algorithm trained label, and calculate fraction black in the high-risk
    patient group.

    Parameters
    ----------
    k : float
        Top k% patients in terms of predicted risk.
    holdout_pred_df : pd.DataFrame
        Predictions for holdout set.
    y_predictors : list
        List of algorithm training label.
    outcomes : list
        List of given outcome of interest.

    Returns
    -------
    pd.DataFrame
        Concentration metric for holdout_pred_df.
    """
    # define lookup for human readable headings in Table 2
    OUTCOME_DICT = {
        'cost_t': 'Total costs',
        'log_cost_t': 'Total costs',
        'cost_avoidable_t': 'Avoidable costs',
        'log_cost_avoidable_t': 'Avoidable costs',
        'gagne_sum_t': 'Active chronic conditions',
        'our_gagne_score': 'ADDED: Calculated gagne score',
        'dem_race_black': 'Race black'
    }

    #top_k = int(k * len(holdout_pred_df))
    top_k = 482
    all_concentration_metric = []  # save all rows of Table 2 to variable

    # iterate through each predictor (algorithm training label)
    # (this is each row in Table 2)
    for y_col in y_predictors:
        # get the predictions column name for y_col
        y_hat_col = '{}_hat'.format(y_col)

        # sort by y_hat_col
        holdout_pred_df = holdout_pred_df.sort_values(by=y_hat_col, ascending=False)
        # get top k% in terms of predicted risk
        top_k_df = holdout_pred_df.iloc[:top_k]

        # define dict to store calculated metrics for given y_col/predictor
        # (each addition to the dict appends a column from Table 2)
        concentration_dict = {
            'predictor': OUTCOME_DICT[y_col]
        }

        # iterate through each outcome
        # (concentration / frac black in highest-risk patients)
        # (this is each column in Table 2)
        for outcome in outcomes:
            if 'log_' in outcome:
                # for the outcomes presented on a log scale,
                # we sum the un-logged values.
                outcome = outcome[len('log_'):]

            # define numerator of concentration metric:
            # sum the top k of outcome
            top_k_outcome = top_k_df[outcome].sum()

            # define denominator of concentration metric
            if outcome == 'dem_race_black':
                # for fraction black in highest-risk patients,
                # denominator is the n of top k%
                total_outcome = top_k
            else:
                # for concentration in highest-risk patients,
                # denominator is the total sum of the entire holdout
                total_outcome = holdout_pred_df[outcome].sum()

            # calculate concentration metric
            frac_top_k = top_k_outcome / total_outcome

            # add column to concentration_dict (row)
            concentration_dict[OUTCOME_DICT[outcome]] = frac_top_k

            # calculate standard error (SE)
            n = len(holdout_pred_df)
            import math
            # SE = sqrt[ p * (1-p) / n]
            se = math.sqrt((frac_top_k * (1-frac_top_k))/n)

            # add SE column to concentration_dict (row)
            concentration_dict[OUTCOME_DICT[outcome] + ' SE'] = se
        all_concentration_metric.append(concentration_dict)

    # convert to pd.DataFrame for pretty formatting
    concentration_df = pd.DataFrame(all_concentration_metric)
    concentration_df = concentration_df.set_index('predictor')

    # define column order of Table 2
    column_order = []
    for outcome in outcomes:
        outcome = OUTCOME_DICT[outcome]
        column_order.append(outcome)
        column_order.append(outcome + ' SE')

    return concentration_df[column_order]

def build_table2(k=0.03):
    """Build Table 2 and save as CSV.

    Parameters
    ----------
    k : float
        Top k% patients in terms of predicted risk.

    Returns
    -------
    pd.DataFrame
        Table 2.
    """
    # define output dir
    #git_dir = util.get_git_dir()
    OUTPUT_DIR = util.create_dir(os.path.join('../', 'results'))

    # load holdout predictions generated from model
    holdout_pred_fp = os.path.join(OUTPUT_DIR, 'our_model_lasso_predictors.csv')
    holdout_pred_df = pd.read_csv(holdout_pred_fp)

    # calculate algorithm performance on alternative labels
    #concentration_df = get_concentration_metric_df(k, holdout_pred_df)
    # calculate best - worst
    #best_worst_row = get_best_worst_difference(concentration_df)

    # calculate counts in different groups
    black_patients = 0
    white_patients = 0
    no_gagne = 0
    yes_gagne = 0

    high_percentile = k
    med_percentile = 0.45

    top_high = int(high_percentile * len(holdout_pred_df))

    for index, row in holdout_pred_df.iterrows():
        if row['dem_race_black']:
            black_patients += 1
        else:
            white_patients += 1

        if row['gagne_sum_t'] == 0:
            no_gagne += 1
        else:
            yes_gagne += 1

    print("No Chronic Conditions: ", no_gagne, "Chronic Conditions: ", yes_gagne)

        

    # define lookup for human readable headings in Table 2
    OUTCOME_DICT = {
        'cost_t': 'Total costs',
        'log_cost_t': 'Total costs',
        'cost_avoidable_t': 'Avoidable costs',
        'log_cost_avoidable_t': 'Avoidable costs',
        'gagne_sum_t': 'Active chronic conditions',
        'our_gagne_score': 'ADDED: Calculated gagne score',
        'dem_race_black': 'Race black'
    }

    y_predictors=['log_cost_t', 'log_cost_avoidable_t', 'gagne_sum_t', 'our_gagne_score']
    outcomes=['log_cost_t', 'log_cost_avoidable_t', 'gagne_sum_t', 'our_gagne_score', 'dem_race_black']
    concentration_dict = dict()

    

    all_concentration_metric = []

    for y_col in y_predictors:

        y_hat_col = '{}_hat'.format(y_col)

        # sort by y_hat_col
        holdout_pred_df = holdout_pred_df.sort_values(by=y_hat_col, ascending=False)
        # get top k% in terms of predicted risk
        top_k_df = holdout_pred_df.iloc[:top_high]

        black_patients_high = 0
        white_patients_high = 0
        black_no_chronic = 0
        black_yes_chronic = 0
        white_no_chronic = 0
        white_yes_chronic = 0
        black_gagne_sum = 0
        white_gagne_sum = 0
        no_chronic_cost = 0
        yes_chronic_cost = 0

        black_scores = [0] * 200
        white_scores = [0] * 200

   
        for index, row in top_k_df.iterrows():
            if row['dem_race_black']:
                black_patients_high += 1
                black_gagne_sum += row['gagne_sum_t']
                if row['gagne_sum_t'] > 0:
                    black_yes_chronic += 1
                else:
                    black_no_chronic += 1
                if row['our_gagne_score'] < 0:
                    black_scores[0] += 1
                else:
                    col = int(row['our_gagne_score'])
                    black_scores[col] += 1
                
            else:
                white_patients_high += 1
                white_gagne_sum += row['gagne_sum_t']
                if row['gagne_sum_t'] > 0:
                    white_yes_chronic += 1
                else:
                    white_no_chronic += 1
                if row['our_gagne_score'] < 0:
                    white_scores[0] += 1
                else:
                    col = int(row['our_gagne_score'])
                    white_scores[col] += 1
            

            # specifics for chronic conditions
            if row['gagne_sum_t'] > 0:
                yes_chronic_cost += row['log_cost_t_hat']
            else:
                no_chronic_cost += row['log_cost_t_hat']


        # add column to concentration_dict (row)
        concentration_dict[y_col] = dict()
        concentration_dict[y_col]['black'] = black_patients_high
        concentration_dict[y_col]['black %'] = black_patients_high / black_patients * 100
        concentration_dict[y_col]['white'] = white_patients_high
        concentration_dict[y_col]['white %'] = white_patients_high / white_patients * 100
        print("METRIC: ", y_col, "Selected Black patients vs white patients: ", black_patients_high, white_patients_high)
        print("Black vs. White Gagne Average: ", black_gagne_sum / black_patients_high, white_gagne_sum / white_patients_high)
        print("Black patients + illnesses (y/n): ", black_yes_chronic, black_no_chronic, "White patients + illnesses (y/n): ", white_yes_chronic, white_no_chronic)
        if black_no_chronic and white_no_chronic != 0:
            print("Avg cost for patients with and without ACC: ", yes_chronic_cost / (black_yes_chronic + white_yes_chronic), no_chronic_cost / (black_no_chronic + white_no_chronic))
        print("BLACK DISTRIBUTION: ", black_scores)
        print("WHITE DISTRIBUTION: ", white_scores)
        #all_concentration_metric.append(concentration_dict)

    concentration_dict["TOTAL"] = dict()
    concentration_dict["TOTAL"]["black"] = black_patients
    concentration_dict["TOTAL"]["white"] = white_patients

    # save output to CSV
    filename = 'table5_concentration_metric.csv'
    output_filepath = os.path.join(OUTPUT_DIR, filename)
    df = pd.DataFrame(concentration_dict)
    print('...writing to {}'.format(output_filepath))
    df.to_csv(output_filepath)

    '''filename = 'table5_concentration_metric.csv'
    output_filepath = os.path.join(OUTPUT_DIR, filename)
    print('...writing to {}'.format(output_filepath))
    table2.to_csv(output_filepath, index=True)'''

    #return table2

    #print additional info!

    chronic_illnesses_col = '{}_hat'.format("log_cost_t")

    # sort by y_hat_col
    holdout_pred_df = holdout_pred_df.sort_values(by=chronic_illnesses_col, ascending=False)
    # get top k% in terms of predicted risk
    top_k_df = holdout_pred_df.iloc[:top_high]

    no_active_conditions = 0
    yes_active_conditions = 0

    for index, row in top_k_df.iterrows():
        if row['gagne_sum_t'] > 0:
            yes_active_conditions += 1
        else:
            no_active_conditions += 1

    # add column to concentration_dict (row)
    print("# of patients selected with chronic conditions (y/n):", yes_active_conditions, no_active_conditions)

    

if __name__ == '__main__':
    build_table2(k=0.35)
