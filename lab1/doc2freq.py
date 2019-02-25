 # document_to_frequency.py
# create 2009
# Noah Pepper
# Artificial Life Lab
# Reed College
# This script takes a .txt source file and outputs a TSV file with words and their frequency sorted.
# Usage: doc2freq.py inputfile
import re,sys,operator
from collections import defaultdict

def txt_clean(txt):
	"""Naive text cleanup"""
	txt = re.sub(r'\W+',' ',txt) 	 # get rid of non-alphanumerics naively
	txt = re.sub(r'[0-9]',' ',txt) # get rid of numbers
	txt = re.sub(r'\s+',' ',txt)   # clean up whitespace
	# convert all to lower case
	txt = txt.lower()

	with open("trans.txt", "w+") as file: file.write(txt)
	return txt
	
def tsv(data,name):
	"""Writes a list (or tuple) of lists (or tuples) to file name.tsv in tsv format"""
	f = open(name+'.tsv','w')
	if type(data) == type([]):
		for i in data:
			f.write('\t'.join([str(x) for x in i])+'\n')
	f.close()
	
def make_freq(data_file):
	#read in the data file
	data = open(data_file,'r').read()
	#clean the data of non-word and non-number items
	data = txt_clean(data)
	#create the dictionary object we'll use to count the words
	freqdict = defaultdict(int)
	#turn our data string into a list of strings by splitting on the space
	data = data.split(' ')
	#count up the occurences of words
	for word in data:
		freqdict[word] += 1
	#turn the dictionary item into a list
	freqs = freqdict.items()
	#sort the list
	freqs = sorted(freqs,key=operator.itemgetter(1), reverse=True)
	#write the word data out to a file
	tsv(freqs, data_file)
	
if __name__=="__main__":
	for filename in sys.argv[1:]: make_freq(filename)
