# Project Notes

## Introduction

## Experimental Design

## Experiments

### Experiment 1: Black-White

Each image filled completely _black_ or _white_.
The task is to classify the image.

Both the CNN and the GAN reach 100% performance.

### Experiment 2: Square-Triangle

Each image has either a _square_ or a _triangle_.
The task is to classify image.

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
(TODO: is this a good range of points? I tried with 3-10 already but only with the CNN, need to test with GAN also)
The _same_ images have both of their polygons the same, but at different rotations.
The _different_ images have different polygons.

The CNN fails:
Training Epoch 40 --- Training Accuracy:  78.1%, Validation Accuracy:  59.4%,  Validation Loss: 0.755

The GAN TODO.

This experiment in particular seems to be a good deciding case of my hypothesis. The GAN is more likely to latch onto the higher-level pattern if I'm correct in my hypothesis.
Of course, there could be first-order patterns to latch onto as well, but the fact that the CNN fails yields this less likely.

### (POTENTIAL) Experiment 5: Cows

A case of over-fitting on first-order patterns is when the CNN recognizes cows in a field view the green that is usually around them.
My hypothesis would be that the GAN would not fall for this first-order trap, because then the Generator would be able to easily beat the discriminator.
The deciding case would be to take a cow picture and color the grass another color, then see how the CNN and GAN perform on classifying it.

## Results

## Conclusions
