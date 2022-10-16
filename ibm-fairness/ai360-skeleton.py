# @misc{aif360-oct-2018,
#     title = "{AI Fairness} 360:  An Extensible Toolkit for Detecting, Understanding, and Mitigating Unwanted Algorithmic Bias",
#     author = {Rachel K. E. Bellamy and Kuntal Dey and Michael Hind and
# 	Samuel C. Hoffman and Stephanie Houde and Kalapriya Kannan and
# 	Pranay Lohia and Jacquelyn Martino and Sameep Mehta and
# 	Aleksandra Mojsilovic and Seema Nagar and Karthikeyan Natesan Ramamurthy and
# 	John Richards and Diptikalyan Saha and Prasanna Sattigeri and
# 	Moninder Singh and Kush R. Varshney and Yunfeng Zhang},
#     month = oct,
#     year = {2018},
#     url = {https://arxiv.org/abs/1810.01943}
# }



# This section of the code has been inpsired from IBM AI Fairness 360's german credit score example
# We were trying to show unfairness in our current synthetic dataset using various fairness metrics


import sys
# sys.path.insert(0, '../')


# from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
# %pip install ipython-venn
# from IPython.display import Markdown, display

# Explainers
from aif360.explainers import MetricTextExplainer

# Datasets
from aif360.datasets import MEPSDataset19
from aif360.datasets import MEPSDataset20
from aif360.datasets import MEPSDataset21

# Fairness metrics
from aif360.metrics import BinaryLabelDatasetMetric
from aif360.metrics import ClassificationMetric

# Scalers
from sklearn.preprocessing import StandardScaler

# Classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Bias mitigation techniques
from aif360.algorithms.preprocessing import Reweighing
from aif360.algorithms.inprocessing import PrejudiceRemover

# LIME
from aif360.datasets.lime_encoder import LimeEncoder
import lime
from lime.lime_tabular import LimeTabularExplainer


dataset_orig = data_new(
    protected_attribute_names=['race'],


    privileged_classes=[lambda x: x = 'white'],
    # features_to_drop=['personal_status', 'sex']

dataset_orig_train, dataset_orig_test = dataset_orig.split([0.7], shuffle=True)

privileged_groups = [{'race': 1}]
unprivileged_groups = [{'race': 0}]

metric_orig_train = BinaryLabelDatasetMetric(dataset_orig_train,
                                             unprivileged_groups=unprivileged_groups,
                                             privileged_groups=privileged_groups)
display(Markdown("#### Original training dataset"))
print("Difference in mean outcomes between unprivileged and privileged groups = %f" % metric_orig_train.mean_difference()