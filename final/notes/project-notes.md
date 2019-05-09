# Project Notes

## Introduction

As mentioned in Melanie's talk, there are still some very _seemingly_ basic things at which the state-of-the-art machine learning algorithms are still incompetent.
I am inspired by the case of breakout, where simply moving the paddle downwards causes the algorithm to completely forget how to play the game.
My hypothesis poses that, in this case for example, the breakout-algorithm didn't _understand_ that there was a paddle as an abstraction, as we think of the paddle as an entity moving through the space of the game. The algorithm simply identified the first-order pattern that connected certain pixels in the bottom half of the screen to being optimal in certain contexts of the rest of the screen (i.e. when pixels light up at some location near the middle of the screen, indicating that the ball is moving downward).
Because the algorithm's _working knowledge_ is connected exactly to that particular line of input where the paddle lies in a horizontal, it's no wonder that when the paddle moves, the machine does not react well.
The algorithm (*TODO*: give the algorithm a name) never needed to abstract, and abstracting would be very costly, so it didn't.
Those pixels a little bit lower than where the paddle was previously were connected to the network in an entirely different way, and there's no reason that the algorithm would have expected them to be involved with the paddle at any point.
I suspect that the reason that humans are able to take advantage of this abstraction so well is because we have much more _training_ thinking of objects as independent from there 'location' as pixels in our vision.
However, the breakout-algorithm never has this experience.
This skill is highly nontrivial, and even if it would be possible for the breakout-algorithm to somehow salvage some of its higher-level knowledge of breakout while just shifting the focus of its first-layer inputs, without previous training at this skill that would be much more unlikely and difficult that just starting from scratch, which is what in fact the algorithm opts to do (via gradient descent).

Of course, if the breakout-algorithm were trained with the paddle at varying heights, then it would eventually reach super-human levels at a paddle-height-variant of breakout.
However, this sidesteps the original concern, because the test of how the algorithm adjusts to situations that it _hasn't_ ever encountered.
Another example of this is that image classifier algorithms can get very good with a test _and_ validation set, but if the images are then rotated, the algorithm completely fails.
The solution to this, of course, is to train the algorithm with all the rotated versions of each images. (*TODO*: citation)

The ultimate problem that I see is that traditional neural networks are excellent at sneakily over-fitting.
They do not overfit by 'memorizing' the original input data, which is the typical concern for over-fitting, but instead latch onto what I can _first-order patterns_.

A _first-order pattern_, in the context of neural network classifiers (i.e. image classifiers) is a pattern that relies on the absolute position of the input nodes.
For example, the breakout algorithm receives its first layer of input via an array of nodes the corresponds exactly to the pixels in the game frame as an image.
The algorithm learns about the paddle only in regards to its exact possible positions on the screen, which is a single horizontal (the paddle never moves vertically).
The algorithm optimizes using this first-order pattern of the paddle as the statistical correlation between pixels having certain values in a certain part of the screen at certain times without learning the higher-order pattern of the paddle being an object that could potentially move in other directions or be in other locations and still be 'the paddle'.

As another example, consider the image classifier.
It is given lots and lots of pictures of animals in their natural environments.
It becomes extremely good at classifying them.
If you present it a picture of a field with cows, it will classify it as 'grazing cows'.
If you present it a picture of a field without cows, it will also classify it as 'grazing cows'.
This is because the classifier likely discovered a first-order pattern in the data that works really well for all of the natural examples that it is given, but doesn't actually correspond to what we have in mind as cows that are animals and separate objects from just their environmental context.
Perhaps the classifier noticed that the label 'grazing cows' correlated almost perfectly to images with lots of green in the bottom half and lots of blue in the top half, with complications around the middle area; these are typical first-order patterns.
When presented with the same picture of cows grazing, but with the cows colored pink, the classifier judges the image as 'flamingos', because images with pink are most likely to have flamingos.
The examples demonstrate how, especially in natural circumstances, first-order patterns are kinds of local maxima that neural networks will likely gravitate towards first in their optimization methods.
Of course, it is not impossible for the networks, given more layers and nodes, to have encoded in them the abstract patterns corresponding perfectly to what we might judge as human-level image classification, but the goal is to get the algorithm to reach this complexity itself through training on examples rather than explicit programming.

A _higher-order pattern_, in the context of neural networks, is a pattern independent from the locations of the nodes in the first couple of layers of the network.
Each successive layer represents a kind of abstraction, so relying on positions in the first layer (input layer) was first-order, and relying on the second could be second-order.
The promise of neural networks is that they can begin to grasp higher-order patterns via their layered, fully-connected structure.
And indeed, in principal, this is possible.
The problem in not necessarily with the network design themselves, but the training process.
I suspect that what most often happens is that the successive layers act more as buffers for noise is the previous layers rather than capturing higher-level patterns (although I recognize these behaviors are not mutually exclusive).



## Experimental Design

The task is to compare the performance of two approaches to machine-learned image classification.
The two approaches are convolutional neural network (CNN) and generative adversarial neural network.

One of these is noticing patterns of matching shapes in images.
I want to see at what point the typical algorithm, the CNN, begins to fail at classification.


## Experiments

Given data is 1000 images per class.

The CNN is allowed 2000 iterations for training. The CNN splits the given data into a training set (1600) and validation set (400).
The training set is where the CNN gets complete supervision. The validation set is where the CNN only gets an overall score.

The GAN is allowed *TODO* iterations for training.


### Experiment 1: Solid Color

Each image filled completely _black_ or _white_.

Both the CNN and the GAN reach 100% performance.
- CNN: Training Epoch 40 --- Training Accuracy: 100.0%, Validation Accuracy: 100.0%,
- GAN:

### Experiment 2: Square-Triangle

Each image has either a _square_ or a _triangle_.

Both the CNN and the GAN reach 100% performance.

### Experiment 3: Reflection-Random

Each image is a wave-like series of rectangles.
The rectangles extrude from the center image down the horizontal axis.
The rectangles in the pattern have varying heights.
The heights of the rectangles are chosen at random.
The _reflected_ images have the same pattern of rectangles in the top half reflected exactly down to the bottom half.
The _random_ images have different patterns of rectangles in top and bottom halves.

Both the CNN and the GAN reach 100% performance.

### Experiment 4: Same-Different

Each image contains two black-filled polygons with between 4-5 points, placed at random (no-overlapping) locations.
(*TODO*: is this a good range of points? I tried with 3-10 already but only with the CNN, need to test with GAN also)
The _same_ images have both of their polygons the same, but at different rotations.
The _different_ images have different polygons.

The CNN fails:
Training Epoch 40 --- Training Accuracy:  78.1%, Validation Accuracy:  59.4%,  Validation Loss: 0.755

The GAN *TODO*.

This experiment in particular seems to be a good deciding case of my hypothesis. The GAN is more likely to latch onto the higher-level pattern if I'm correct in my hypothesis.
Of course, there could be first-order patterns to latch onto as well, but the fact that the CNN fails yields this less likely.

### (POTENTIAL) Experiment 5: Cows

A case of over-fitting on first-order patterns is when the CNN recognizes cows in a field view the green that is usually around them.
My hypothesis would be that the GAN would not fall for this first-order trap, because then the Generator would be able to easily beat the discriminator.
The deciding case would be to take a cow picture and color the grass another color, then see how the CNN and GAN perform on classifying it.

## Results

## Conclusions
