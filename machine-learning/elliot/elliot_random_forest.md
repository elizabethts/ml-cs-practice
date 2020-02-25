Decision Trees


#### What are the basic concepts? What problem does it solve?
- Trees have a weakness in predictive learning: inaccuracy (not great with classifying new samples)
- Called ensemble learning because: you ensemble a bunch of DTs to train, and your output is:
    - Mode of the classes (classification)
    - Mean prediction of individual trees (regression )

#### What are the assumptions?
- the sampling is representative

#### What are the steps of the algorithm?
-	Steps:
    - Create a bootstrapped dataset (randomly selected sample of the dataset)
    - Create a DT of the bootstrapped dataset, but only using a random subset of variables at each step
    - Repeat many times, change the number of variables used per step randomly, as this de-correlates the trees
    - Aggregate the individual tree outputs by averaging
        - This is called "Bagging" (bootstrapping the data, plus use the aggregate to make a decision --> "bootstrap aggregation"
    - For predictions: run it through the many RF trees, and tally the “votes” aka decisions to see which decision comes out top
- Why bagging?
    - Reduce variance but bias is the same
- How do you make random forest overfit? (decrease bias)
    - increase variance and lower bias
    - No pruning (all trees grown as large as possible)
    - Keep increasing number of trees and tree depth
- Tune hyperparameters with GridSearch or RandomizedSearchCV
- Out of bag score is a way to validate random forests

#### What is the cost function?

#### What are the advantages/disadvantages?
Pros:
- overcomes the problem of overfitting in DTs
- less variance than a single DT
- Very high accuracy
- No data preprocessing required
- Great accuracy even when data is missing

Cons:
- difficult to interpret (more so than DTs)
- computationally expensive compared to DT, but the benefit is that you can parallelize bagging (not boosting) so time complexity is better than others

Notes from:  
[StatQuest: Decision Trees]( https://www.youtube.com/watch?v=7VeUPuFGJHk)

[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)
