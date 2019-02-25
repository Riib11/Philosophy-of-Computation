# Report

## Preliminary Tasks

### Record size of documents (word tokens).

`patentsample.txt` has 993 lines, 107,088 words (word tokens), and 729088 characters.

### Record size of dictionary (word types).

`patentsample.tsv` has 7,856 word entries (word types)

### Briefly describe the contents of the document.
### Try to predict word frequencies in this document.

## Analyzing Example Document

### Briefly describe `doc2freq.py`; what do you understand and what is a total mystery?

I am fairly fluent in python, so I understand the program completely. `doc2freq.py` defines three functions:
- `txt_clean(txt)`: In the string `txt`, replace non-alphanumeric characters with spaces, replace all consecutive whitespace with a single space, and convert all character to lower case.
- `tsv(data, name)`: Create a file called `name+'tsv'` and write to it a line for each index of `data` the index (word type) and the value (word token).
- `main(data_file)`: Read the data file to a string, clean the string with `txt_clean`, and split the clean string into a list of words separated by spaces. Then, iterate through the word list and keep track of the frequencies of words via a dictionary where indecies are words and values are the token counts of their indecies. Sort the dictionary by decreasing token count. Finally, write the dictionary to a `.tsv` file.

### Run `doc2freq.py` on example document. How many words are in example document's dictionary?

After running `doc2freq.py` on `patentsample.txt`, the resulting word frequencies contain 7,856 unique word types.

### Describe any "dirt" in data (.tsv) and describe how to clean it.

There are some obvious non-words, such as some single-letters (e.g. r, c, n, etc.), word-fragments (e.g. sub, rf, wt), and word-concatenations (e.g. therebetween, basestation).

Some of these are basically unavoidable, such as the word-concatenations. The only way to efficiently distinguish them from true compound-words would be to use a standard dictionary, but many words are outside of standard lexicon but are still legitimate in the patent context.

The single-letters and word-fragments seem, after looking through the context of their instances, to be part of words that use non-alphanumeric characters such as hyphens. I think a good way to modify the cleaning process would be to allow for hyphens to be considered valid characters for words.

### Run `zipf.r` on example document's dictionary. Describe the R-plot's notable features

The plot does produce the remarkable -1 sloped correlation between log(frequency) and log(rank). It is most densely populated and appropriately-correlated in the 4-6 range. The 0-4 range is the most sparse, and the 6-10 range is more dense but degenerates into a more distinct step-function.

## Main Task

### 1. Make a Zipf plot of some **real world text corpus** (using and/or modifying given code)



### 2. Make Zipf plot of **random languages of different sizes**. Put all plots of same graph, with same axis.


### 3. Make a log-log scatter plot of **dictionary size vs. corpus size** for the data sets analyzed by other students.


### 4. Add useful features to **Zipf plotting software** such as
  - display dictionary size and corpus size
  - fit a line to the data, plot the line over a scatter plot
  - display the line's slope (exponent)
  - display error bars for the slope exponent
