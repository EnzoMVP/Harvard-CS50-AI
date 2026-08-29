first attempt: 0.05 acc, 3.5 loss
 - 1 hidden layer: 64 units
 - 1x convolution & pooling: 32 filters, 2x2 pool size
 - 0.4 dropout

second attempt: accuracy: 0.9773 - loss: 0.0995
 - add one hidden layer with 128 units
 - 2x convolution & pooling
 - 0.5 dropout

third attempt: accuracy: 0.9517 - loss: 0.2139
 - 128 units in both hidden layers

4th attempt: accuracy: 0.6119 - loss: 1.1500
 - 1x convolution & pooling

5th attempt: accuracy: 0.9341 - loss: 0.2551
 - 3x conv & pooling
 - 2 hidden: 64 - 128 units

6th attempt: accuracy: 0.9631 - loss: 0.1611
 - 2x conv & pooling
 - 0.3 dropout

final decision: attempt 2 config