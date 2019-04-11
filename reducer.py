# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:23:33 2019

@author: Emilio.Marinone
"""

from itertools import islice

class Reducer():
    ''' lines number of lines you want to extract, init first line (must be integer)
    '''
    
    def __init__(self, lines=10, path='', input_file='', output_file='', init = 1):
        if path == '':
            self.path = r'./data//'
        else:
            self.path = path
        if input_file == '':
            self.input_file = ''.join([self.paht, 'Posts.xml'])
        else:
            self.input_file = ''.join([self.paht, input_file])
        if output_file == '':
            self.output_file = ''.join([self.paht, 'Posts_small.xml'])
        else:
            self.output_file = ''.join([self.paht, output_file])
        if init < 1 or type(init) != int:
            self.init = 1
        else:
            self.init
        if lines < 1 or type(lines) != int: 
            self.lines = 10
        else:
            self.lines = lines
            
    def reduce(self):
        
        file = []
        with open(self.input_file, 'r', encoding='utf8') as f:
            for row in islice(f, self.init -1, self.init + self.lines):
                file.append(row.strip())
        
        joined_file = ''.join(file)
        with open(self.output_file, 'w', encoding='utf8') as f:
            f.write(joined_file)
            
        return True
    
reducer = Reducer(lines = 100)
print(reducer.reduce())
