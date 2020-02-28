K-means Clustering

#### What are the basic concepts? What problem does it solve?
- goal is to partition input points into K distinct clusters

#### What are the assumptions?
- Data must be numeric, not categorical
- clusters are spherical and of a similar size (so that the algorithm can form clusters)

#### What are the steps of the algorithm?
1. Find k:
    - Plot to see if there are any patterns
    - Elbow method: grid search k=1-10 to calculate sum of squares within each cluster.
    - Or randomly choose k initial cluster centroid locations
2. with these initial k centroids, repeat the following process:
    - each data point is assigned to a cluster centroid in order to minimize a WCSS objective function (within-cluster sum of squares)
    - then each centroid is re-computed. for each cluster, the new centroid is computed by averaging the observations assigned to it, hence, the "mean"

We repeat these steps until the algorithm "converges". How do you detect convergence?
- run until none of the observations change clusters
- if you compute the WCSS, it should decrease over time (e.g. the error becomes smaller)

#### What is the cost function?
WCSS:
- Minimize the sum of the squared distance between the data points and the cluster’s centroid (arithmetic mean of all the data points that belong to that cluster)

#### What are the advantages/disadvantages?
Pros:
- fast/efficient for large number of variables
- easy to implement
- scales to large data sets
- guarantees converges
- easily adapts to new examples

Cons:
- gets stuck in local minima, so your first result may not be the best one. Have to run it multiple times with different initial centroids and the one with the lowest error is chosen
- doesn't do well with outliers
- have to pick optimal k-value manually
- order of data impacts final results
- sensitive to scale
- does not work well with clusters of different sizes and density

Notes from:  
[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)

[Stack Exchange](https://stackoverflow.com/questions/21630246/how-does-k-means-work/21630531)

[r-bloggers](https://www.r-bloggers.com/exploring-assumptions-of-k-means-clustering-using-r/)

[Google Developers, great graphics here](https://developers.google.com/machine-learning/clustering/algorithm/advantages-disadvantages)
