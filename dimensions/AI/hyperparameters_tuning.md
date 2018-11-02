# Hyperparameters

- alpha (most important, 1st)
- beta (2nd)
- beta1, beta2, epsilon (Adam, 0.9, 0.999, 10^8)
- number of layers (3rd)
- number of layer units (2nd)
- learning rate decay (3rd)
- mini-batch size (2nd)


# Hyperparameters search

- Try random values: Don't use a grid
- Coarse to fine
- Radom sampling
- Adequate searching
- Appropriate/right scale for hyperparameters

#  Re-test hyperparameters occasionally
- Pandas vs Caviar

# Batch Normalization
- Normalizing inputs to speed up learning
- Not just the input layer, but all neural network layers
- As regularization
- Each mini-batch is scaled by the mean/variance computed on just that mini-batch
- Has slightly regularization effect. Using big mini-batch size can reduce the regularization effect.
- it adds some noise to the values zl

# Multi-class Classification

- Softmax activiation function
- Softmax regression
- Softmax classifier

# Deep Learning frameworks

- Caffe
- CNTK
- DL4J
- Keras
- Lasagne
- mxnet
- PaddlePaddle
- Tensorflow
- Theano
- Torch

Defined in `Keras` -> trained with `Tensorflow` -> Using `IBM Watson Studio`
