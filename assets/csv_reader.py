import csv
import string
from nltk.tokenize import RegexpTokenizer
from gensim.models.doc2vec import TaggedDocument
from gensim import  models

import pandas as pd

tokenizer = RegexpTokenizer(r'\w+')  #

dataset = pd.read_csv('./datasets/reference.csv')

sentences = dataset['text'].dropna()
sentences = [s.translate(None, string.punctuation) for s in sentences]
sentences = [s.lower() for s in sentences]

tagged_sentences =[TaggedDocument(s , 'SENT_%s' % id) for id , s in enumerate(sentences)]
model = models.Word2Vec(tagged_sentences)


