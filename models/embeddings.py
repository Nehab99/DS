# embeddings.py

import fasttext

def load_pretrained_embeddings(embedding_path):
    return fasttext.load_model(embedding_path)

def train_with_pretrained_embeddings(train_file, embedding_model, model_output, lr=0.1, epoch=25):
    model = fasttext.train_supervised(
        input=train_file,
        lr=lr,
        epoch=epoch,
        pretrainedVectors=embedding_model
    )
    model.save_model(model_output)
    return model
