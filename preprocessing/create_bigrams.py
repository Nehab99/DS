# create_bigrams.py

from nltk import bigrams

def generate_bigrams(text):
    tokens = text.split()
    bigram_list = [' '.join(bigram) for bigram in bigrams(tokens)]
    return ' '.join(bigram_list)
