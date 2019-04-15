# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:25:01 2019

@author: Emilio.Marinone
"""

import re
import os
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
#from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup as BS
#nltk.download('stopwords')
#nltk.download('punkt')

class FeatureProcessor():
    
    def __init__(self, features = None):
        self.cleanr = re.compile('<.*?>')
        self.data_path   = r'./data/'
        self.corpus_path = r'./glove/'
        self.post_path = ''.join([self.data_path, 'Posts_small.xml'])
        self.tags_path = ''.join([self.data_path, 'Tags.xml'])
        self.corpus    = ''.join([self.corpus_path, 'corpus.txt'])
        self.output    = ''.join([self.corpus_path, 'vectors.txt'])
        self.w2v	   = ''.join([self.corpus_path, 'w2v.txt'])
        try: 
            self.disfluencies = features['disfluencies']
            self.init         = features['init']
            self.end          = features['end']
        except:
            print('FeatureProcessor not instantiated correctly, see Class notes')
			
        self.stopwords = set(stopwords.words('english'))

    def _body_cleaner(self, bad_body):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', bad_body)
        #extended_disfluencies = self.disfluencies
        for url in urls:
            bad_body = bad_body.replace(url, "")
        semi_clean = str(BS(bad_body,"html.parser").text)
        clean_with_n = re.sub(self.cleanr, '', semi_clean)
        clean = clean_with_n.replace('\n', ' ')
        low_no_stopwords = self._preprocess(clean)
        #add newline before returning cleaned body    
        return ''.join([low_no_stopwords, '\n'])
        
    def _preprocess(self, bad_body):
        words = bad_body.split()
        list_words = []
        for word in words:
            if word.lower() not in self.stopwords:
                temp_word = word.lower()
                if temp_word[-1] == '.' or temp_word[-1] == ',':
                    temp_word = temp_word[-1]
                list_words.append(temp_word)
                
        return ' '.join(list_words)
		
	
    def create_corpus(self):
        
        #load data
        with open(self.post_path, 'r', encoding='utf8') as f:
            posts_strings = f.readlines()[2:-1]
#        with open(self.tags_path, 'r') as f:
#            tags_strings = f.readlines()[2:-1]
#        if len(posts_strings) > 1:
#            posts_strings = posts_strings[2:-1]
        print('Start building corpus')
        corpus = []
        for post in posts_strings:
            i_idx = post.rfind(self.init) + len(self.init)
            f_idx = post.rfind(self.end)
            bad_body = post[i_idx:f_idx]
            #expand with tags here if needed
            clean_body = self._body_cleaner(bad_body)
            corpus.append(clean_body)
        #join removing items to save allocated memory   
        print('Building single string')
        body_string = ''
        for el in corpus:
            body_string += corpus.pop(0)
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
        print(first_line)
        joined_corpus = ''.join(output)
        file = first_line + joined_corpus
	
        with open(self.w2v, 'w', encoding='utf8') as f:
            f.write(file)
        return True

features = {'disfluencies': ["&lt;", "p&gt;", "&quot;", "&#xA;", "/p&gt;", "href", "//blockquote&gt"], 'init': 'Body="','end': '" OwnerUserId'}  
feat = FeatureProcessor(features = features)

#if we have vectors.txt the model has already been trained and we can create the correspondent w2v format required by Gensim
if os.path.exists(feat.output):
	print(feat.create_w2v())
else:
#	#if we don't have an output, we should first create a corpus and train
	print(feat.create_corpus())
      
        
