Logistic


#### What are the basic concepts? What problem does it solve?
- a type of Generalized Linear Model (GLM)
- Same formula as linear regression, but instead of the continuous Y, it is regressing for the probability of an event (which is binary)
- the regression fits an S-shaped logistic function

#### What are the assumptions?
- Outcome variable is binary
- linearity between log(odds) and predictor variables
- no collinearity between independent variables

#### What are the steps of the algorithm?
- Use the sigmoid function to map predicted values to probabilities: this maps any real value into another value between 0 and 1
- We map the probability score to a discrete class (true or false, cat or dog), and select a threshold value above which we classify values into binary classes
- These two things make up the prediction function

#### What is the cost function?
-
- achieved by maximum likelihood
- It is not MSE (L2) like in linear regression because our prediction function is non-linear
- We use cross-entropy, also known as log loss
    - divided into two separate cost functions: one for y=1, y=0
    - It penalizes wrong predictions more than it rewards right predictions

#### What are the advantages/disadvantages?
- Similar to linear regression

Pros:
- gives probabilities versus classification (can choose the cut off)
- can be used for multi-class (>2) classification: called multinomial regression  

Cons:
- interpretation is more difficult

#### Multinomial logistic regression vs one-vs-rest binary logistic regression
-

#### How to deal with overfitting in logistic regression?
- if low variance: easiest way is to add regularization
- increase number of features through feature engineering helps with high bias??

Notes from:  
[StatQuest: Gradient Boost](https://www.youtube.com/watch?v=3CC4N4z3GJc)

[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)

[Interpretable machine learning](https://christophm.github.io/interpretable-ml-book/logistic.html)
