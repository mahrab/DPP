# -*- coding: utf-8 -*-

import json
import nltk
import string

def gen_sents(filename):

	with open(filename) as in_file:
		my_data = json.load(in_file)

	with open("stopwords.txt") as s_file:
		my_stopword_list = s_file.read().split()

	doc_sents = []
	for doc in my_data:
		doc_sents += doc['responses']

	with open("sents.txt", "w") as out_file:
			for sent in doc_sents:
				s = sent.decode('utf8')
				s = s.lower()
				s = nltk.word_tokenize(s)
				s = ' '.join([i for i in s if i not in my_stopword_list and i.isalpha()])
				out_file.write(s + '\n')

	return

if __name__ == '__main__':
	gen_sents("aspect_query_responses_10192017_with_vecs.json")