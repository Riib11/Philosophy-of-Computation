# TODO

## Preliminary Tasks

- Record size of documents (word tokens).
- Record size of dictionary (work types).
- Briefly describe the contents of the document.
- Try to predict word frequencies in this document.

## Analyzing Example Document

- Briefly describe `doc2freq.py`; what do you understand and what is a total mystery?
- Run `doc2freq.py` on example document.
- How many words are in example document's dictionary?
- Describe any "dirt" in data (.tsv) and describe how to clean it.
- Run `zipf.r` on example document's dictionary.
- Describe the R-plot's notable features

## Main Task

1. Make a Zipf plot of some **real world text corpus** (using and/or modifying given code)
2. Make Zipf plot of **random languages of different sizes**. Put all plots of same graph, with same axis.
3. Make a log-log scatter plot of **dictionary size vs. corpus size** for the data sets analyzed by other students.
4. Add useful features to **Zipf plotting software** such as
    - display dictionary size and corpus size
    - fit a line to the data, plot the line over a scatter plot
    - display the line's slope (exponent)
    - display error bars for the slope exponent
