# Data sets
- Training data set
- Dev data set
- Test data set

For small number of data:
- train/test: 70/30
- train/dev/test: 60/20/20

For big data:
- train/dev/test: 98%/1%/1%
or
- train/dev/test: 99.5/0.25%/0.25%

The rule of thumbs:
- The train and test sets are from different distribution
- The dev and test sets are from the same distribution
- It's ok to have on test sets, but it will cause the overfitting of `dev` set


# Bias and Variance

- underfitting
- overfitting
- high variance(dev data performance): train set err 1%, dev set err 11%
- high bias(training data performance): for example,train set err 15%, test set err 16%
- Training sets err gives you a sense of bias
- Dev sets err gives you a sense of variance

# Basic Recipe for Machine Learning
- High bias?
  - bigger network
  - train longer
  - NN architecture search
- High variance?
  - More data
  - Regularization
  - NN architecture search
  
# Regularizing your neural network
- Logistic regression
  - L2 regularization, norm - ||w||2, perferred
  - L1 regularization, ||w||
- Neural network
  - Frobenius norm
  - Dropout regularization
  - Data augmentation, like disortion the pictures
  - Early stopping
Orthogonalization, think about one task at one time:
- Optimize the cost function
  - Gradient decrease
- Not overfitting
  - Regularization

# Setting up your optimization problem
- Normalize your inputs, training sets, mean-0 normalizing you input features
- Vanishing/Exploding gradients
- Weights initialization for NN
- Numerical approximation of gradients
- Gradient checking helps me tons of times, don't use in training, only to debug

