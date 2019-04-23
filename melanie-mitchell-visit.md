# Artificial Intelligence - The Barrier of Meaning

_Presentation by Melanie Mitchell_

## Introduction

The perceptron was the first implementation of something like artificial intelligence.

Lots of famous predictions about the future of human-level AI and how its coming soon. Of course, none have been true yet.

Gary Marcus is an AI skeptic.

## Survey of State-of-the-Art AI

The deep learning revolution was with the practical implementation of multi-layered, feed-forward neural networks.

### Object classification and Detection on ImageNet

Inspired by WordNet that is used by linguists. To gather a labeled set of images, hired Amazon mechanical Turk. Then hosted a competition of classifying the images. For classification, improved from 0.28 error in 2010 and 0.03 in 2016.

### Image Captioning

Given an image, generates a sentence and that describes the image. As of 2016 (Vinyals O et al) captioning is pretty good! But its a little unreliable. Example: Captionbot.ai.

### Speech Recognition

Improved from 16 word error rate to 4 word error rate as of 2018.

### Machine Translation

Google Translate. Does well for individual sentences, but is bad for linking together the structure of several sentences.

### Question-Answering

Given a context and a question about the context, extract the answer from the context. As of now, machines do better than humans in this task. But are they really _understanding_, _comprehending_, and/or _reading_?

### Atari Games

DeepMind's Deep Q-learning was able to beat Atari games at super-human level.

## Weaknesses and Vulnerabilities of Modern Approaches

### A new AI Winter?

_AI Winter is Well on Its Way_ by Filip Piekniewski.
(https://blog.piekniewski.info/2018/05/28/ai-winter-is-well-on-its-way/)

### Unreliability

Google translate doesn't take context into account when words have multiple meaning.

Image captioning uses the context of an image too heavily, and makes bad inferences when the connections don't hold (a grassy environment should have cows, but when it doesn't, might still label it as having cows).

Autonomous cars can be unreliable in edge cases. For example, salt lines in the road confuse a Tesla car about where the lanes are.

### Subtle Bias

Word vector models learn biases from the data set their trained on. Google translate also uses word vectors, so has similar biases.
(http://bionlp-www.utu.fi/wv_demo)

But how do we work differently from these examples? Other than that we have more data and we make moral judgments and we take more subtle features into account. **Example**: describing a female-faced person in a military uniform as a _woman_, and the captioner describes it as a man.

### Trouble with Generalization

Deep neural networks have trouble with abstraction. Paper: _25 years of CNNs: Can we compare to human abstraction capabilities?_

Deep reinforcement learning sometimes is not able to transfer to slightly different scenarios. Example: Breakout but the paddle is slightly higher. This area of AI is called _Transfer Learning_.

But in the Breakout example, maybe the problem is that the program learned everything just from playing Breakout, but humans have been trained at the abstract concept beforehand and are just using that to generalize rather than what they learned from Breakout.

## On "Understanding"
