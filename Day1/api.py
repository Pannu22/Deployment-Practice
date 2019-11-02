# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:26:25 2019

@author: Pannu
"""

import re
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import flask
from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/home')
def test_api():
    return 'Yay!!!! API is working'

@app.route('/preprocess',methods=['POST'])
def remove_stopwords():
    
    data = json.loads(request.data.decode())
    text = data['text']
    print('\n', data, '\n')
    word_tokens = re.split(' ',text)
    stop_words = stopwords.words('english')
    preprocessed_sent = [t for t in word_tokens if t not in stop_words]
    return str(preprocessed_sent)

@app.route('/topwords',methods=['POST'])
def find_top_words():
    
    data = json.loads(request.data.decode())
    text, num_words = data['text'], data['num']
    print('\n', data, '\n')
    word_tokens = re.split(' |;|:|,',text)
    word_len = [len(word) for word in word_tokens]
    sorted_len = np.argsort(word_len)
    top_words = []
    for idx in sorted_len[-num_words:]:
        top_words.append(word_tokens[idx])
    return str(top_words)

@app.route('/lastwords',methods=['POST'])
def find_last_words():
    
    data = json.loads(request.data.decode())
    text, num_words = data['text'], data['num']
    print('\n', data, '\n')
    word_tokens = re.split(' |;|:|,',text)
    word_len = [len(word) for word in word_tokens]
    sorted_len = np.argsort(word_len)
    last_words = []
    for idx in sorted_len[-num_words:]:
        last_words.append(word_tokens[idx])
    return str(last_words)

if __name__=='__main__':
    app.run(host='localhost',port=5000)