Decision Trees


#### What are the basic concepts? What problem does it solve?
- Trees have a weakness in predictive learning: inaccuracy (not great with classifying new samples)
- So you ensemble a bunch of DTs to train, and your output is:
    - Mode of the classes (classification)
    - Mean prediction of individual trees (regression )

#### What are the assumptions?
- the sampling is representative

#### What are the steps of the algorithm?
-	Steps:
    - Create a bootstrapped dataset (randomly selected sample of the dataset)
    - Create a DT of the bootstrapped dataset, but only using a random subset of variables at each step
    - Repeat many times, change the number of variables used per step randomly, as this de-correlates the trees
    - No pruning (all trees grown as large as possible)
    - Aggregate the individual tree outputs by averaging --> this is called bagging
        - This is called "Bagging" (bootstrapping the data, plus use the aggregate to make a decision)
    - For predictions: run it through the many RF trees, and tally the “votes” aka decisions to see which decision comes out top
- Why bagging?
    - Reduce variance but bias is the same
- Tune hyperparameters with GridSearch or RandomizedSearchCV

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
- computationally expensive

Notes from:  
[StatQuest: Decision Trees]( https://www.youtube.com/watch?v=7VeUPuFGJHk)

[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)
