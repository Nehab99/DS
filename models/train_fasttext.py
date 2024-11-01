# train_fasttext.py

import fasttext
import os

def prepare_fasttext_data(input_path, output_path, label_prefix="__label__"):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            # Assuming input data has label and text in comma-separated format
            label, text = line.strip().split(',', 1)
            outfile.write(f"{label_prefix}{label} {text}\n")

def train_fasttext_model(train_file, model_file, lr=0.1, epoch=25, word_ngrams=1, label_prefix="__label__"):
    model = fasttext.train_supervised(
        input=train_file,
        lr=lr,
        epoch=epoch,
        wordNgrams=word_ngrams,
        label=label_prefix
    )
    model.save_model(model_file)
    return model
