# Project Description

Philosophy of Computation
Henry Blanchette

## Updates

Update: I've changed my project idea because I was inspired by an idea that Melanie Mitchell brought up when she visited our class, and my original project goal was to create two music generation algorithms which I think may be disappointing in the span of time I have to work on it, they will both end up sounding bad and it will be uninspiring to compare them.

Proposal: My new topic proposal is to investigate two versions of an image classifier, and see if the approaches prove to behave any differently when it comes to recognizing abstract patterns. The two versions are: deep convolutional neural network and generalized generative adversarial network. This is more feasible because image classification will be much easier to design, judge, and train especially given the kinds of tests that I have in mind.

## Description

One of the chief criticisms of modern AI is its inability to generalize its learned "knowledge" beyond its original training data.

A specific and illustrative case of this is in image classification. Many images are captioned by humans, and these can be used as training data for machine learning algorithms to try and caption un-captioned images.

The state of the art progress on this front has produced excellent classifiers for the training data, but they are easily fooled (relative to humans) by unlikely examples.

The common theme of the successful, adversarial examples is that they take advantage of how the algorithm has not sufficiently abstracted the parts of an image from their context.

I hypothesize that if machine learning algorithms achieve this ability to abstract relevant patterns, such as objects in images, the way that humans do, they would perform much better at generalizing their "knowledge" in all their tasks.

A relatively new machine learning technique, called a generative adversarial network (GAN), takes advantage of traditional machine learning's shortcomings.

Suppose we are trying to classify images of a certain type, and we have a starting data set of pre-classified images. A GAN consists of two machine learning algorithms: the generator and the discriminator. The two algorithms compete to outdo each other, where the generator generates images in attempt to fool the discriminator that they are from the original data set, and the discriminator tries to pick out the generator images from the original images.
<!-- Each training round, the generator chooses with 50% chance to show the discriminator an image from -->

This result of this training process is two algorithms: an image classifier and an image generator.

My experiment is to compare a traditional deep neural network image classifier with a GAN image classifier, both given the same training data.
I will test each network on a set of tasks mainly including classifying images that have simple patterns in them for the classifiers to discover (that I will create with some simple program), such as images with two identical shapes and images with two non-identical objects (this is like what Mitchell described in her presentation). In order to succeed, the classifier will need to learn the abstract the pattern that I encoded into the program that created the image classes.

My hypothesis is that the GAN will perform substantially better than the neural network. I think this because the GAN's design specifically addresses the problem of learning useless but convenient features (from the classifier's point of view), which seem to be a critical leg that neural networks stand on in most image classification tasks but then fall flat on when it comes to this abstraction test.
