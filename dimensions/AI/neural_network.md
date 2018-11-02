## AI(Strong AI, week AI)(1950)
  - brute-force search
  - perceptron
    - supervised learning algorithm for single-layer neural network. Linear classification
  - clustering algorithms
    - unspuervised learning. k-means
  - decision trees
  - rule-based systems
    - a rule set
    - a knowledge based
    - an inference engine
    - a user interface
    
## Machine Learning(1980)
  - subfield of AI and CS
	- roots in statistics and mathematical optimazation
	- Backpropagation
	- CNN: image processing, video recognition, natural language processing
	- LSTM: long short-time memory, Recurrent network
  
## Deep learning(2000, neural netowrk in many layers)
  
  - isn't an algorithm, per se
  - a family of algorithm that implement deep networks with unsupervised learning.
  - CNN + LSTM(RNN)
  
## Cognitive computing

  - Building on neural network and deep learning
  - knowledge from congnitive science, simulate human thought processes
  - inlcuding ML, NLP, vision, human-computer interaction
  - IBM Watson
  
## Neural Network

- Features -> Standard NN
- Autonomous driving -> complex, customized, hybird neural network
- Deep Neural Network
- Convolutional Neural Network(CNN)
  - image
- Recurrent Neural Network(RNN)
  - Sequence data, like audio, Machine translation

### Binary Classification
  - Notation
  - Logistic Regression
  - Linear Regression, sigma, theta
  - Given x, want y^(hat), y^=P(y=1|x)
    - parameters: w, b
    - output: y^ = sigmoid(w(Transpose)*x + b)
  - Loss function/Error function
    - L(y^, y) = 1/2(y^ - y)^2 -- square error function
    - L(y^, y) = -(ylogy^+ (1-y)log(1-y^)) -- 
  - Cost function ---> to minimize
    - J(w, b) = 1/m * sum(L(y^i, yi))
  - Gradient Descent
    - derivative w := w - aphla * (partial derivative of w)
    - How to compute derivatives...
    - Vectorization(矢量化)
  - Computation graph
    - forward propagation: left-to-right computation
    - backward propagation: right-to left computation
    
 ## Python
 
- numpy
- rank 1 array, column vector, row vector
- gradient descent converges faster after normalization


    
