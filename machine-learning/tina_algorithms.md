---
noteId: "ae53f530534811ea822635ee916a2dec"
tags: []

---

# K-means Clustering

* What are the basic concepts? What problem does it solve?

K-means clustering can be used to solve unsupervised machine learning problems. It is one of the most popular and widely used unsupervised learning techniques. 

This algorithm is basically partitioning our dataset into K pre-defined disting and non-overlapping clusters (subgroups). Each datapoint can only belong into a single group.

* What are the assumptions?

We need to have numeric data to apply this algorithm.

* What are the steps of the algorithm?

1. **Choose K** (specify number of clusters)

2. **Initialize centroids** (by shuffling the dataset and then randomly selecting K data points for the centroids without replacement)

3. **Clustering assignment** (calculate the euclidian distance between each data point and the centroids - depends on whether it is closer to one centroid (i.e. K = 2 we will assign the data point to one of the clusters))

4. **Move centroid** (calculate the average of all points belonging to each cluster and then move centroid to the average point location)

* What is the cost function?

We want to minimize the squared distance. 

TOOD - look into this more.

* What are the advantages/disadvantages?

Advantages - easy, fast, efficient

Disadvantages - sensitive to outliers, K value not known, sensitive to scale, does not work well if we have the data of different density/scale.


# K-Nearest Neighbours

* What are the basic concepts? What problem does it solve?

KNN is a **supervised learning** algorithm based on the idea of similarity, or proximity - similar things are near to each other. This algorithm is calculating the distance between two points on a graph.

* What are the assumptions?

This algorithm can be used for both classification (we calculate the mode) and regression (we return the mean) problems.

It's a **non-parametric model**, so it does not make any underlying assumptions about the distribution. 

* What are the steps of the algorithm?

1. Load the data and initialize K (chosen number of neighbors)

2. For each example in data we:

    2.1 Calculate the distance between the query example and the current example from the data

    2.2 Add the distance and the index of the example to an ordered collection

3. Sort the collection of distances and indices from smallest to largest (ascending) by distances 

4. Pick the first K entries from the sorted collection & get the labels of K entries

5. Depending on the problem:

    5.1 For regression problems, return the mean of the K labels

    5.2 For classification problems, return the mode of the K labels 


* What is the cost function?

This model does not have a cost function. In fact, K-NN is not trained at all. 

**Distance to measure similarity:**
Euclidean distance = L2 distance, going from 0 to (2,2)
Hamming distance
Manhattan distance = L1 distance, going along the each lines (absolute values of X, Y)
Minkowski distance

* What are the advantages/disadvantages?

Advantages - easy to interpret output, naturally handles multi-class cases, calculation time, predictive power (given that we have enough representative data)

Disadvantages - large search problem to find nearest neighbours, storage of data, must know we have a meaningful distance function


# Ada-Boost 

* What are the basic concepts? What problem does it solve?

This **classification** algorithm converts a set of weak classifiers into a strong one. This is done by retraining the algorithm iteratively by choosing the training set based on the accuracy of previous training. 

The **weight-age** of each trained classifier at any iteration depends on the accuracy achieved. 

In a nutshell, the algorithm aggregates weak hypotheses for strength. It scales up incorrect and scales down correct.

* What are the assumptions?

TODO: research

* What are the steps of the algorithm?

1. 

2.

3. 

4. 

* What is the cost function?

The cost function is **exponential loss**.

L(y, f(x)) = exp(-yf(x))

* What are the advantages/disadvantages?


# Decision Trees

* What are the basic concepts? What problem does it solve?

In decision trees, we are trying to specify sequences of decisions and consequences, basically we're breaking down our dataset to smaller subsets.

We can use Regression Tree or Classification Tree.

The main parts are:

- Root Node
- Branch Node
- Internal Node
- Leaf Node 

The **depth of a node** is the minimum number of steps required to reach the node from the root.


* What are the assumptions?

This model performs well on unprocessed data (we don't have to normalize, center or scale features)

It is a non-parametric method - it does not make explicit assumptions about the function form of f, it just estimate of f in terms of mean.

* What are the steps of the algorithm?

1. We start with recursive binary splitting based on the predictor X and the cutpoint s. We aim for greatest possible reduction in CLassification Error rate. 

2. Now we have 2 partitions and we want to repeat this process to look for the best predictor and best cutpoint to split the data further. The goal is to minimize Classification Error Rate/Misclassification Rate. We find and sort by Gini index - we try to find the smallest one.

3. We continue until a stopping criterion is reached (i.e. no region contains more than 5 observations, we have points in only 1 class).


* What is the cost function?

Regression tree - minimize (MSE or RSS - residual sum of squares)

Classification tree - minimize classification error rate 

TODO: Explain better 


* What are the advantages/disadvantages?

Advantages - simple to understand and interpret, can be used even with little data, we can add new scenarios, we can do outcomes modeling (best, worst), it is a "white box" model, and finally we can combine it with other decision techniques (TODO) and it can handle non-linear relationships. 

Disadvantages - they are unstable (small change in data can lead to large change in the structure), they may be relatively inaccurate (hence random forest, but that one has lower interpretability), there might be biases in variables - attributes with more levels are favoured. Finally, the calculations can be more complex. 


# Random Forest 

* What are the basic concepts? What problem does it solve?

* What are the assumptions?

* What are the steps of the algorithm?

* What is the cost function?

* What are the advantages/disadvantages?


# Algorithm

* What are the basic concepts? What problem does it solve?

* What are the assumptions?

* What are the steps of the algorithm?

* What is the cost function?

* What are the advantages/disadvantages?