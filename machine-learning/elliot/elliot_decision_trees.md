Decision Trees

#### What are the basic concepts? What problem does it solve?
Intuition:  
- DTs are built from yes/no questions
- Breaks down a dataset into smaller subsets
-	Classify until no more

#### What are the assumptions?
-	DTs are nonparametric, so no assumptions made about the classifier or underlying distribution

#### What are the steps of the algorithm?
-	Top of the tree is called the Root, others are called Internal Nodes, the ends are called Leafs
    - When none of the leaf nodes classify 100% correctly, they are considered impure
    -	To determine which separation is best, we need to compare impurity
      - One popular way is Gini impurity: weighted average of impurities for the leaf nodes (lower is better)
      - So it optimizes for lowest Gini impurity scores for leaf nodes (if the node has the lowest score, no point separating anymore, ends there)
      - For numeric data (e.g. weight), works the same and the yes/no is < or > a weight cutoff
      - For ranked data (e.g. ordinal data), use similar cut-offs <=
- Pick features based on lowest RSS or Gini impurity
- Stop splitting by setting a threshold for depth of tree
- Tree pruning: Deal with overfitting by pruning (reduces sections of the tree that provide little predictive power)
- Evaluation:
  - Gini index: measure of node purity
  - Entropy

#### What is the cost function?
Regression:  
- minimize residual sum of squares

Classification:  
- minimize classification error rate (Gini impurity)

#### What are the advantages/disadvantages?
Pros:  
- Easy to interpret
- Can handle nonlinear relationships
- Performs well on unprocessed data (e.g. no normalizing)

Cons:  
- Relatively inaccurate compared to other algorithms, better to use a RF
- Tend to overfit

Notes from:  
[StatQuest: Decision Trees]( https://www.youtube.com/watch?v=7VeUPuFGJHk)

[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)
