U.S. healthcare providers use predictive algorithms to identify high-risk patients to prioritize in providing preemptive care, affecting health decisions for hundreds of millions of American patients. However, studies have found that many of these algorithms are racially biased, as they are less likely to recommend additional care to Black patients with the same health conditions as their white counterparts.

Our project aims to apply a variety of techniques to mitigate racial bias and improve fairness in these algorithms. We focus on the specific case study of the commercial healthcare algorithm studied by Obermeyer et al., which seeks to identify which patients would benefit the most from preemptive care. Our goals are to utilize techniques from the papers we studied, namely training labels that are fairer and more representative of patient health and changing the model infrastructure to enforce that biased input variables hold less weight. We also aim to incorporate our own novel techniques, including using the IBM Fairness classifier and dropping certain proxy variables for race.

So far, with this midterm project, we've laid the groundwork for creating improved training labels, dropping proxy variables, and incorporating the IBM fairness classifier, generating preliminary results for the former two techniques.

Results:

Pre processing - Dropping cost variables

The current model trains on over 100 different variables, 13 of which are cost specific variables. That is, these variables are indicative on the amount spent on specific medical treatments such as physical therapy and surgical operations. In an effort to improve predictors, we decided to pre-process our dataset and remove these cost variables prior to training our model. This resulted in total costs and avoidable costs becoming better classifiers in that the fraction of black patients within the 97th percentile was higher than before (see Figure 4). This may suggest that changing the output label alone is not a sufficient strategy, and infact common commercial predictors such as total costs could be used if associated training cost variables are removed. We intend to explore this idea further.
![alt text](https://github.com/mjoshicodes/cpsc464-group1/blob/main/figures/results_by_predictor.png)

In processing - Gagne Score

We created a new index variable based on the Gagne score to gauge patient health and train the model with. Utilizing the synthetic dataset we calculated the associated Gagne score of each patient and trained our model on this predictor. The goal of suggesting this new predictor was to increase the ratio of Black patients that fell within the 97 percentile risk score, meaning that they would be eligible for the health program. While this predictor was not as effective as others suggested by Obermeyer et al. (see Figure 3) it still had a higher ratio of Black patients compared to the predictor of Total Cost, which is what most commercial algorithms use.
![alt text](https://github.com/mjoshicodes/cpsc464-group1/blob/main/figures/results_dropped_costs_by_predictor.png)
