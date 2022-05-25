import re
import string
import numpy as np
import pandas as pd
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import LSTM
    
def clean_text(text):
    '''Make text lowercase, 
    remove text in square brackets, 
    remove links, 
    remove punctuation and 
    remove words containing numbers.'''

    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def remove_stopwords(text):
    stop_words = stopwords.words('english')
    text = ' '.join(word for word in text.split(' ') if word not in stop_words)
    return text

def stem_text(text):
    stemmer = nltk.SnowballStemmer('english')
    text = ' '.join(stemmer.stem(word) for word in text.split(' '))
    return text

def embed(corpus): 
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer.texts_to_sequences(corpus)

def preprocess_data(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = stem_text(text)
    text = pd.Series(text)
    text = pad_sequences(
        embed(text), 
        length_long_sentence, 
        padding='post'
    )
    return text