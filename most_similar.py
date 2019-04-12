# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:25:36 2019

@author: Emilio.Marinone
"""

from gensim.models.keyedvectors import KeyedVectors as KV

class Similarity():
    
    def __init__(self):
        self.w2v = r'./glove/w2v.txt'
        self.wv = KV.load_word2vec_format(self.w2v, binary=False)
        
    def most_similar(self, word='you'):
        if type(word) == str:
            return self.wv.most_similar(word)
        else:
            return None

word = 'c#'
sim = Similarity()
print('Searching for most similar words of : ' + word)
print(sim.most_similar(word))


