# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:25:01 2019

@author: Emilio.Marinone
"""

import re
import os

class FeatureProcessor():
    
    def __init__(self, features = None):
        self.data_path   = r'./data//'
        self.corpus_path = r'./glove//'
        self.post_path = ''.join([self.data_path, 'Posts_small.xml'])
        self.tags_path = ''.join([self.data_path, 'Tags.xml'])
        self.corpus    = ''.join([self.corpus_path, 'corpus_small.txt'])
        self.output    = ''.join([self.corpus_path, 'output_small.txt'])
        self.w2v	   = ''.join([self.corpus_path, 'w2v_small.txt'])
        try: 
            self.disfluencies = features['disfluencies']
            self.init         = features['init']
            self.end          = features['end']
        except:
            print('FeatureProcessor not instantiated correctly, see Class notes')
        
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
        with open(self.post_path, 'r', encoding='utf8') as f:
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
        with open(self.corpus, 'w', encoding='utf8') as f:
            f.write(corpus)
            
        return True
		
    def create_w2v(self):
	
        with open(self.output, 'r', encoding='utf8') as f:
            output = f.readlines()
        
        c = len(output[0].split()) - 1 #(word 0.12 0.23 0.35)
        r = len(output)
    		
        first_line = str(r) + ' ' + str(c) + '\n'
        joined_corpus = ''.join(output)
        file = first_line + joined_corpus
    		
        with open(self.w2v, 'w', encoding='utf8') as f:
            f.write(file)
    			
        return True

features = {'disfluencies': ["&lt;", "p&gt;", "&quot;", "&#xA;", "/p&gt;", "href", "//blockquote&gt"], 'init': 'Body="','end': '" OwnerUserId'}  
feat = FeatureProcessor(features = features)

#
if os.path.exist(feat.output):
	print(feat.create_w2v)
else:
	#if we don't have an output, we should first create a corpus and train
	print(feat.create_corpus())
      
        
