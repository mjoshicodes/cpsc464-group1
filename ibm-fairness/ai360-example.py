# First, read-in the data and check for null values
import numpy as np
import pandas as pd
import aif360
from aif360.algorithms.preprocessing import DisparateImpactRemover
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
pd.options.mode.chained_assignment = None  # default='warn', silencing Setting With Copy warning
df = pd.read_csv('credit_risk.csv')

# Remove rows with null values
df = df.dropna(how='any', axis = 0)

target_counts = df['Loan_Status'].value_counts()

# Drop unnecessary column
df = df.drop(['Loan_ID'], axis = 1)

# Encode Male as 1, Female as 0
df.loc[df.Gender == 'Male', 'Gender'] = 1
df.loc[df.Gender == 'Female', 'Gender'] = 0
# Encode Y Loan_Status as 1, N Loan_Status as 0
df.loc[df.Loan_Status == 'Y', 'Loan_Status'] = 1
df.loc[df.Loan_Status == 'N', 'Loan_Status'] = 0

y = df['Loan_Status']

# Replace the categorical values with the numeric equivalents that we have above
categoricalFeatures = ['Property_Area', 'Married', 'Dependents', 'Education', 'Self_Employed']
# Iterate through the list of categorical features and one hot encode them.
for feature in categoricalFeatures:
    onehot = pd.get_dummies(df[feature], prefix=feature)
    df = df.drop(feature, axis=1)
    df = df.join(onehot)

from sklearn.model_selection import train_test_split
encoded_df = df.copy()
x = df.drop(['Loan_Status'], axis = 1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_std = scaler.fit_transform(x)
# We will follow an 80-20 split pattern for our training and test data, respectively
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state = 0)

actual_test = x_test.copy()
actual_test['Loan_Status_Actual'] = y_test

# Priviliged group: Males (1)
# Unpriviliged group: Females (0)
male_df = actual_test[actual_test['Gender'] == 1]
num_of_priviliged = male_df.shape[0]
female_df = actual_test[actual_test['Gender'] == 0]
num_of_unpriviliged = female_df.shape[0]

unpriviliged_outcomes = female_df[female_df['Loan_Status_Actual'] == 1].shape[0]
unpriviliged_ratio = unpriviliged_outcomes/num_of_unpriviliged

priviliged_outcomes = male_df[male_df['Loan_Status_Actual'] == 1].shape[0]
priviliged_ratio = priviliged_outcomes/num_of_priviliged

# Calculating disparate impact
disparate_impact = unpriviliged_ratio / priviliged_ratio
print("Disparate Impact, Sex vs. Predicted Loan Status: " + str(disparate_impact))

from sklearn.linear_model import LogisticRegression
# Liblinear is a solver that is very fast for small datasets, like ours
model = LogisticRegression(solver='liblinear', class_weight='balanced')

model.fit(x_train, y_train)

# Let's see how well it predicted with a couple values 
y_pred = pd.Series(model.predict(x_test))
y_test = y_test.reset_index(drop=True)
z = pd.concat([y_test, y_pred], axis=1)
z.columns = ['True', 'Prediction']
z.head()

import matplotlib.pyplot as plt
from sklearn import metrics
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))

# We now need to add this array into x_test as a column for when we calculate the fairness metrics.
y_pred = model.predict(x_test)
x_test['Loan_Status_Predicted'] = y_pred
original_output = x_test
original_output

# Priviliged group: Males (1)
# Unpriviliged group: Females (0)
male_df = original_output[original_output['Gender'] == 1]
num_of_priviliged = male_df.shape[0]
female_df = original_output[original_output['Gender'] == 0]
num_of_unpriviliged = female_df.shape[0]

unpriviliged_outcomes = female_df[female_df['Loan_Status_Predicted'] == 1].shape[0]
unpriviliged_ratio = unpriviliged_outcomes/num_of_unpriviliged

priviliged_outcomes = male_df[male_df['Loan_Status_Predicted'] == 1].shape[0]
priviliged_ratio = priviliged_outcomes/num_of_priviliged

# Calculating disparate impact
disparate_impact = unpriviliged_ratio / priviliged_ratio
print("Disparate Impact, Sex vs. Predicted Loan Status: " + str(disparate_impact))

import aif360
from aif360.algorithms.preprocessing import DisparateImpactRemover
# binaryLabelDataset = aif360.datasets.BinaryLabelDataset(
#     df=yourDataFrameHere,
#     label_names=['yourOutcomeLabelHere'],
#     protected_attribute_names=['yourProtectedClassHere'])
# Must be a binaryLabelDataset
binaryLabelDataset = aif360.datasets.BinaryLabelDataset(
    favorable_label=1,
    unfavorable_label=0,
    df=encoded_df,
    label_names=['Loan_Status'],
    protected_attribute_names=['Gender'])
di = DisparateImpactRemover(repair_level = 1.0)
dataset_transf_train = di.fit_transform(binaryLabelDataset)
transformed = dataset_transf_train.convert_to_dataframe()[0]

x_trans = transformed.drop(['Loan_Status'], axis = 1)
y = transformed['Loan_Status']
# Liblinear is a solver that is effective for relatively smaller datasets.
model = LogisticRegression(solver='liblinear', class_weight='balanced')
scaler = StandardScaler()
data_std = scaler.fit_transform(x_trans)
# Splitting into test and training
# We will follow an 80-20 split pattern for our training and test data
x_trans_train,x_trans_test,y_trans_train,y_trans_test = train_test_split(x_trans, y, test_size=0.2, random_state = 0)

