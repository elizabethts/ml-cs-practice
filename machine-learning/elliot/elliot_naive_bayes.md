Naive Bayes

#### What are the basic concepts? What problem does it solve?
- Classification algorithm, using Bayes rule
- Use Gaussian for continuous variables
- Parametric as do make assumptions about the data (independence)

#### What are the assumptions?
- naive: independence among the features (not realistic)

#### What are the steps of the algorithm?
- need to understand conditional probability and Bayes' rule

Bayes:
          P(B|A) * P(A)
P(A|B) = _________________________________________________
               P(B)

Naive Bayes:
                                    P(Likelihood of Evidence) * Prior prob of outcome
P(outcome|evidence aka Posterior) = _________________________________________________
                                     P(Evidence)

- run the formula for each possible outcome, which is a class and has a class label
- frequency counts

#### What is the cost function?
- no cost function??

#### What are the advantages/disadvantages?
Pros:
- Great for text classification, high dimensional training sets: sentiment analysis, classifying news articles, email spam filtering
- Fast, as calculations are very simple, can make predictions in real time
- Good for multi class prediction

Cons:
- assumption of independence among predictors is not realistic for real data (although it performs well even on complex tasks)
- does not generalize to unseen data


Notes from:  
[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)

[StackOverflow](https://stackoverflow.com/questions/10059594/a-simple-explanation-of-naive-bayes-classification)
