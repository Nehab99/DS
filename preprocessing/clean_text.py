# clean_text.py

import re
import string

def remove_urls(text):
    return re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def lowercase_text(text):
    return text.lower()

def preprocess_text(text):
    text = remove_urls(text)
    text = remove_punctuation(text)
    text = lowercase_text(text)
    return text
