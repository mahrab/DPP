import json
import nltk, re, pprint
from nltk import word_tokenize
import string
import numpy as np

def check_summary(filename):
	
	with open(filename) as in_file:
		my_data = json.load(in_file)
	
	report_list = []
	sep = " "
	table = {ord(c): None for c in string.punctuation}

	for doc in my_data:
		report = {}
		report['aspect'] = doc['aspect']
		print "Aspect:"
		print report['aspect']
		sents = word_tokenize(sep.join(doc['responses']).lower().translate(table))
		report['1 diversity'] = float(len(get_unique_nGram(sents, 1)))/float(len(get_all_nGram(sents, 1)))
		print "1-Gram Diversity:"
		print report['1 diversity']
		report['2 diversity'] = float(len(get_unique_nGram(sents)))/float(len(get_all_nGram(sents)))
		print "2-Gram Diversity:"
		print report['2 diversity']
		report['3 diversity'] = float(len(get_unique_nGram(sents, 3)))/float(len(get_all_nGram(sents, 3)))
		print "3-Gram Diversity:"
		print report['3 diversity']
		report['4 diversity'] = float(len(get_unique_nGram(sents, 4)))/float(len(get_all_nGram(sents, 4)))
		print "4-Gram Diversity:"
		print report['4 diversity']
		report['all length'] = map(len,doc['responses'])
		print "All Sentence Lengths:"
		print report['all length']
		report['average length'] = float(sum(report['all length']))/float(len(report['all length']))
		print "Average Sentence Length:"
		print report['average length']
		report['std dev length'] = np.std(report['all length'])
		print "Std. Dev. of Sentence Length:"
		print report['std dev length']
		print ''
	
	return

def get_unique_nGram(l, n = 2):
    l = list(l)
    return set(zip(*[l[i:] for i in range(n)]))

def get_all_nGram(l, n = 2):
    l = list(l)
    return zip(*[l[i:] for i in range(n)])

if __name__ == '__main__':
	check_summary("summary.json")