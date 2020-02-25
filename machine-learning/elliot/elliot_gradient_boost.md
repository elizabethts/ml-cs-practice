Decision Trees


#### What are the basic concepts? What problem does it solve?
-	GB deals with overfitting by using a learning rate to scale the contributions from the new tree (rate is between 0 and 1)
- Boosting: fit consecutive trees at each step. Adds new models to the ensemble sequentially, then analyze the errors before fitting models

#### What are the assumptions?
-

#### What are the steps of the algorithm?
Steps:
- Starts with a single leaf, not a tree. The leaf represents an initial guess for the predictions of all the samples
- After you have the initial prediction, then you build a tree using the features to predict the residuals (instead of original target)
- Creates fixed-size trees based on errors made by the previous tree, then using a learning rate to scale the contribution from the new tree each time
- Repeat until it makes the number of trees you asked for, or additional trees fail to improve the fit
    - Without the learning rate (0, 1), boosting fits the model too well: low bias, high variance  

#### What is the cost function?
- depending on models (the residual is the cost function)
    - regression: MSE
    - negative log/loss

#### What are the advantages/disadvantages?
Pros:
- Can build predictive functions of great complexity:
    - If you fit a deep decision tree "at one go", your variance will be very high and test error very poor
    - Boosting lets you carefully control the variance of the model while building the predictive function very slowly to check errors
    - It is very important to use a small learning rate and weak individual learners to use boosting effectively
    - They let us layer on complexity very slowly and test errors
- Low bias and lower variance than other tree-based models
- No preprocessing required
- No data imputation required

Cons:
- Overfitting is a risk
- Computationally expensive as uses many trees

Notes from:  
[StatQuest: Gradient Boost](https://www.youtube.com/watch?v=3CC4N4z3GJc)

[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)

[StackExchange](https://stats.stackexchange.com/questions/335859/understanding-gradient-boosting)
