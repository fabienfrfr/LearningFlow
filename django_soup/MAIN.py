#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:10:06 2022
@author: fabien
"""

from bs4 import BeautifulSoup as bs
import pandas as pd, os
#import requests

############ Initialization
path = './QCM_HTML/'
file_list = os.listdir(path)

############ CONSTRUCT DATASET
DF = []
for f in file_list :
    ## OPEN CORRECTLY FILE
    with open(path+f) as fp:
        soup = bs(fp, 'html.parser')
    
    ## TREE QUESTION
    Q_LIST = []
    for data in soup.find_all("table"):
        CONTENT_LIST = []
        i, R = 0, 0
        for d in data.find_all("p") :
            # response finding
            if d.find('b') != None : R = i
            content = d.get_text()
            # clean and add data in list
            CONTENT_LIST += [content.replace('\n', ' ').replace('\t', '')]
            i+=1
        # question list
        Q_LIST += [[f.split('.')[0].split('_')[1]]+CONTENT_LIST+[R]]
    
    # construct dataframe
    df = pd.DataFrame(Q_LIST, columns =['NAME','QUESTION', 'A', 'B', 'C', 'D','S'])#, 'COMMENT', 'COEFF'])
    DF += [df]
## concatenate
DF = pd.concat(DF, ignore_index=True)
print(DF)

############ SUPERVISED-LEARNING
"""
ideas : use basic models for learning questions for says probability of response (help button)
bag of word, etc
"""


############ GAME-WEBPAGE
"""
basic django
"""





############ ANALYSIS DATA IN REAL TIME (link beetween question)


















