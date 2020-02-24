Support Vector Machine (SVM)


#### What are the basic concepts? What problem does it solve?
- Support vector machines focus only on the points that are the most difficult to tell apart, whereas other classifiers pay attention to all of the points.
- If a classifier is good at the most challenging comparisons, then the classifier will be even better at the easy comparisons
- unlike other classifiers, the SVM is explicitly told to find the best separating line

#### What are the assumptions?
- no distributional assumptions other than iid
- scale data first

#### What are the steps of the algorithm?
- Searches for closest points, called support vectors
- Draw a line connecting them by vector subtraction
- Declares the best separating line to be the line that bisects and is perpendicular to the connecting line

If the problem is non-linear:
- no good hyperplane can be found, so use kernel trick
- this involves projecting the original, non-linear space to a higher dimensional one with a non-linear transformation, so you can do a plain SVM
- kernels include: linear, polynomial, radial basis function, sigmoid

#### What is the cost function?
- Uses hinge loss and L2 regularization: maximize the margin

#### What are the advantages/disadvantages?
Pros:
- Avoids overfitting because of regularization
- Kernel trick allows complex problem solving, like for non-linear models
- Generalizes well
- Better than neural networks as it gives a unique solution

Cons
- Have to choose the right kernel function, which can affect overfitting
- Only classifies, does not provide class probabilities
- Have to tune the hyperparameters correctly (kernel type, kernel specific parameters)
- Long training time
- Difficult to understand and interpret the model



Notes from:  
[Cracking the DS phone interview](https://medium.com/@bruceyanghy/crack-the-machine-learning-phone-interview-guide-9e4dc316f65b)

[SVM notes](http://web.mit.edu/6.034/wwwbob/svm-notes-long-08.pdf)

[Stats StackExchange](https://stats.stackexchange.com/questions/23391/how-does-a-support-vector-machine-svm-work)

[Stats StackExchange](https://stats.stackexchange.com/questions/3947/help-me-understand-support-vector-machines)

[Stats StackExchange](https://stats.stackexchange.com/questions/24437/advantages-and-disadvantages-of-svm)

[A Practical Guide to Support Vector Classification](https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf)

[Good deck with visuals](https://www.cs.ubc.ca/~schmidtm/Courses/340-F17/L21.pdf)
