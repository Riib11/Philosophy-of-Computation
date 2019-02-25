"""
Following tutorial: https://stackabuse.com/implementing-model-with-gensim-library-in-python/
"""

import bs4 as bs
import re
import nltk
import pickle
import sys

if len(sys.argv) < 2:
  raise Exception("error: please provide a text file")

in_file_name = sys.argv[1]

# get raw text
with open(in_file_name, "r") as in_file:
  corpus_text = "".join([line for line in in_file])

# Cleaning the text
processed_corpus = corpus_text.lower()  
processed_corpus = re.sub('[^a-zA-Z]', ' ', processed_corpus)
processed_corpus = re.sub(r'\s+', ' ', processed_corpus)

# log processed_corpus
# print("processed_corpus:", processed_corpus)

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_corpus)
all_words     = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
from nltk.corpus import stopwords
for i in range(len(all_words)):  
  all_words[i] = list(filter(
    lambda w: not w in stopwords.words('english'),
    all_words[i]))

# build Word2Vec model
from gensim.models import Word2Vec
model = Word2Vec(all_words, min_count=5)

with open(in_file_name+".model", "wb+") as out_file:
  pickle.dump(model, out_file)
