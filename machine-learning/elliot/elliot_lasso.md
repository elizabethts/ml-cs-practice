Lasso Regression

#### What are the basic concepts? What problem does it solve?
- "least absolute shrinkage and selection operator"
- A regularization method for regression models that shrinks coefficients towards zero by using a penalty
- As some coefficients may shrink to zero, thus lasso performs feature selection
- NOT a model. Just a regularization technique applied to regressions

#### What are the assumptions?
- Similar to basic regression, iid (independent and identically distributed)

#### What are the steps of the algorithm?
- The only addition to regression is it adds a L1 norm/penalty/regularization
    - We use the sum of the absolute value of the parameter values
- the coefficients are the solutions to the L1 optimization problem
- Tune parameter lambda to control the amount of regularization
  - When lambda = 0, it's just an ordinary least squares regression
  - when lambda is very large, all coefficients go to 0. This is known as a "sparse" model, aka having lots of zeros

#### What is the cost function?
- Minimize the MSE and L1 penalty

#### What are the advantages/disadvantages?
Pros:
- Produces sparse solutions as sets coefficients to 0: offers feature selection, which ridge cannot do
- Regularization avoids overfitting:
    - reduces variance without increasing bias too much
    - reduce prediction error
- Tends to outperform ridge regression in bias, variance, MSE

Cons:
- Lasso randomly drops features that correlate, so this is a problem if you want to understand which features are important for prediction (versus just getting the prediction)
- Use Elastic Net instead to get the best of both Ridge & Lasso: keeps parameters from getting too large, and nudges them towards zero without hurting model performance too much
- In a large data model: does not understand complex/non-linear associations 


Notes from:  
[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)

[Stats StackExchange](https://stats.stackexchange.com/tags/lasso/info)

[Stanford slides](https://statweb.stanford.edu/~owen/courses/305a/Rudyregularization.pdf)

[Regularization](https://e2eml.school/regularization.html)
