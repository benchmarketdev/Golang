# Mini-batch gradient descent

For large training data set:
- baby training sets -> mini-batch, say 1000 examples for each
- epoch is a word that means a single pass through the training set
- mini-batch gradient descent runs much faster than batch gradient descent(entire training set)

Understanding mini-batch gradient descent:
- mini-batch size in-between `1`(too small) to `m`(too large)
- if `m`, batch gradient descent, too long per iteration
- if `1`, stochastic gradient descent, noisiness, you lose all your speed up from vectorization

Rule of thumb:
- if training set < 2000, use batch gradient descent
- Typical mini batch size: 64, 128,256, 512, is a power of 2
- All of X{t}, Y{t} that fits in CPU/GPU memory


# Exponentially Weighted Average
- Bias correction in exponentially weighted average
- The bias correction can help you get a better estimate early on

# Gradient descent with momentum
- compute an exponentially weighted average of your gradients, and then use that weights to update your weight instead.

# RMSprop
- stands for `root mean squre prop`
- can also speed up gradient descent

# Adam optimization algorithm
- Adaptive momentum estimate
- combine the `momentum` and `RMSprop` together
- Hyperparameters choice 
  - alpha, need to tune
  - beta_1, 0.9, dw
  - beta_2, 0.99, power of dw
  - epsilon, e-8
  
# Learning rate decay
- During the inital steps of learning, you could afford to take much bigger steps
- there are many ways to implement learning rate decay

# The problem of local optima
- local optima
- it's unlikely to get stuck in a bad local optima
- pleteaus can make learning slow
