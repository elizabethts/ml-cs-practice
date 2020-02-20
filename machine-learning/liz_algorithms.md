## Machine Learning Algorithms

### Questions
#### What are the basic concepts? What problem does it solve?
#### What are the assumptions?
#### What are the stps of the algorithm?
#### What is the cost function?
#### What are the advantages/disadvatages?


#### Linear Regression


#### Regression with Lasso


#### Regression with Ridge


#### Stepwise Regression


#### Logistic Regression


#### Naïve Bayes
- probabalistic classifier
- assumes features occur independently of once another
- assume independence --> calculate prior and likelihood --> calculate posterior --> predict class with highest posterior
- figure out cost function
- advantages
    - fast, easy
    - multiclass classification
    - better than logistic regression and requires less data (when independent assumption holds true)
- disadvantages
    - when a category was not in the training set but appears in the test set, naive bayes will not be able to make a prediction. This problem is called "zero frequency". Can be solved by smoothing.... one method is called laplace estimation
    - naive bayes is a bad estimat
    - real life events are not independent
- types
    - gaussian
    - multinomial
    - bernouli
- applications
    - real time predictions
    - text classification/sentiment analysis/spam filtration
    - recommendation engines

#### K-Nearest Neighbors
- no underlying distributions about the model

#### K-means Clustering


#### Decision Tree


#### Random Forest



#### Ada-Boost


#### Gradient Boosting
why is it called gradient boost?
- when you calculate the residual, you do it by taking the gradient of the cost function


- non parametric
- doesnt make underlying assumption about the data

what is the cost function?
- you want your cost function to be differentiable


#### SVM (Support Vector Machine)
##### **What are the basic concepts? What problem does it solve?**
The goal of SVM is to create a hyperplane that will divide the training vectors into 2 classes. A hyperplane in this case is a linear surface that splits the space into 2 parts, so its for binary classification problems. Hyperplanes always span one dimension less than their ambient space. The best choice hyperplane for SVM is one that maximizes the margin between the two classes. SVM is generally good for smaller datasets with few outliers 

##### **What are the assumptions?**
- no underlying assumptions about the data

##### **What are the stps of the algorithm?**
- maximum margin hyperplane
- support vectors
- support vector classifier
- kernel trick

##### **What is the cost function?**
- hinge loss
we want to find the decision surface that is maximally far away from any data points

##### **What are the advantages/disadvatages?**
##### **Pros**
- works well with highly dimensional data like for document classification
- works with unstructured and semi-structured data like text, images, and trees
- less risk of overfitting

##### **Cons**
- choosing a good kernel function is not easy
- long training time for large datasets
- difficult to understand and interpret the model
- in cases where the number of features are greater than the number of observations, SVMs can perform poorly


#### PCA (Principal Component Analysis)
##### **What are the basic concepts? What problem does it solve?**
PCA is a method of dimensionality reduction that takes a lot of data and turns it into something that captures the essence of the original data. It does this by taking a dataset with a lot of features/dimensions and flattening it into 2 or 3 dimensions so we can look at it. Each dimension is represented by a principal component, which is a linear combination of all of the original variables that maximizes variance. Principal component 1 spans the axis with the most variance and principal component 2 spans the axis with the second most variance. 

##### **What are the assumptions?**
- you have multiple variables that are continuous
- the variables have a linear relationship. A linear relationship is needed because PCA uses the Pearson correlation coefficient with is a measure of linear dependence between two variables
- you have a large enough dataset for sampling adequacy
- your data should be suitable for reduction meaning the variables have adequate correlations
- no significant outliers. Outliers have a disproportionate effect on results


##### **What are the stps of the algorithm?**
- Preprocessing:
    - change any categorical data to numerical
    - standardize feature sets
    - normalize mean
- calculate covariance matrix
- calculate eigenvectors and eigenvalues
- select the number of principal components that span >99% variance

##### **What is the cost function?**
- elbow method?

##### **What are the advantages/disadvatages?**
##### **Pros**
- reflects our intuition about data
- reduces data down to a smaller size, faster to process, smaller storage
- able to estimate probabilities on highly dimensional data without having independence of variables

##### **Cons**
- too expensive for many applications
- not good at tasks with fine grained classes
- understanding assumptions behind methods, linearity






#### Neural Networks