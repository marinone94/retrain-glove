# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:25:01 2019

@author: Emilio.Marinone
"""

from xml.etree import cElementTree as ET
import re

class FeatureProcessor():
    
    def __init__(self, features = None):
        self.data_path   = r'./data//'
        self.corpus_path = r'./glove//'
        self.post_path = ''.join([self.data_path, 'Posts.xml'])
        self.tags_path = ''.join([self.data_path, 'Tags.xml'])
        self.corpus    = ''.join([self.corpus_path, 'corpus.txt'])
        try: 
            self.disfluencies = features['disfluencies']
            self.init         = features['init']
            self.end          = features['end']
        except:
            raise RunTimeError('FeatureProcessor not instantiated correctly, see Class notes')
        
    def _body_cleaner(self, bad_body):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', bad_body)
        #extended_disfluencies = self.disfluencies
        for url in urls:
            bad_body = bad_body.replace(url, "")
        for el in self.disfluencies:
            bad_body = bad_body.replace(el, "")
        #add newline before returning cleaned body    
        return ''.join([bad_body, '\n'])
        
        
    def create_corpus(self):
        
        #load data
        with open(self.post_path, 'r', encoding="utf8") as f:
            posts_strings = f.readlines()[2:-1]
#        with open(self.tags_path, 'r') as f:
#            tags_strings = f.readlines()[2:-1]
    
        corpus = []
        for post in posts_strings:
            i_idx = post.rfind(self.init) + len(self.init)
            f_idx = post.rfind(self.end)
            bad_body = post[i_idx:f_idx]
            #expand with tags here if needed
            clean_body = self._body_cleaner(bad_body)
            corpus.append(clean_body)
        #join     
        corpus = ''.join(corpus)
        #write to corpus.txt
        with open(self.corpus, 'w', encoding="utf8") as f:
            f.write(corpus)
            
        return True

features = {'disfluencies': ["&lt;", "p&gt;", "&quot;", "&#xA;", "/p&gt;", "href", "//blockquote&gt"], 'init': 'Body="','end': '" OwnerUserId'}  
feat = FeatureProcessor(features = features)
print(feat.create_corpus())



        
        
