#### Parametric vs Non-Parametric


- A parametric model is one that can be parametrized by a finite number of parameters.
- A nonparametric model is one which cannot be parametrized by a fixed number of parameters


A parametric model is one where we assume the ‘shape’ of the data, and therefore only have to estimate the coefficients of the model.

A non-parametric model is one where we do not assume the ‘shape’ of the data, and we have to estimate the most suitable form of the model, along with the coefficients.

A parametric model is usually preferred, as one would only have to estimate the parameters of the model, instead of having to estimate the entire model with a non-parametric approach.

However, the assumption made regarding shape of the data with a parametric approach can potentially lead to selecting a model which does not reflect the true ‘shape’ of the data.

In a parametric model, you know which model exactly you will fit to the data, e.g., linear regression line. In a non-parametric model, however, the data tells you what the 'regression' should look like.

Let me give some concrete examples.
Parametric Model: 𝑦𝑖=𝛽0+𝛽1𝑥𝑖+𝑒𝑖
Here you know what the regression will look like: a linear line.

Non-Parametric Model: 𝑦𝑖=𝑓(𝑥𝑖)+𝑒𝑖 where f(.) can be any function. The data will decide what the function f looks like. Data will not tell you the analytic expression for f(.), but it will give you its graph given your data set.
The reason why people say that there is inherently no difference between parametric and non-parametric regression is that the function f(.) can be perfectly approximated by an infinite-parameter model, which is parametric.

Naive Bayes
- parametric when multinomial over the vocabulary, or a Gaussian
- non-parametric when 1D kernel density estimation
- parametric is more common

Decision trees:
- is non-parametric method, it doesn’t make explicit assumptions about the function form of f, it just estimate of f in terms of mean.

Notes from:
[Basics of Statistical Machine Learning](http://pages.cs.wisc.edu/~jerryzhu/cs731/stat.pdf)

[Quora](https://www.quora.com/What-is-the-difference-between-a-parametric-model-and-a-non-parametric-model)

[Quora](https://www.quora.com/What-is-an-intuitive-explanation-of-the-difference-between-parametric-and-nonparametric-statistical-tests)
