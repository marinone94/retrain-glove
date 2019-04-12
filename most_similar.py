# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:25:36 2019

@author: Emilio.Marinone
"""

from gensim.models.keyedvectors import KeyedVectors as KV

class Similarity():
    
    def __init__(self):
        self.w2v = r'./glove/w2v.txt'
        self.wv = KV.load_word2vec_format(w2v, binary=False)
        
    def most_similar(self, word='you'):
        if type(word) == str:
            return wv.most_similar(word)
        else:
            return None

sim = Similarity()
print(sim.most_similar('word'))


