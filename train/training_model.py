from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import torch
import pandas as pd
import numpy as np


sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')


def get_dataframe(path):
    df = pd.read_csv(path, sep=';')
    print(df)
    return df


def get_list(df):
    question_list = df['Question'].to_list()
    answer_list = df['Answer'].to_list()
    return question_list, answer_list


# transfer sentence to vector
def process_embedding(df):
    question_list, answer_list = get_list(df)
    answer_list = [str(i) for i in answer_list]
    q_model = sentence_bert_model.encode(question_list)
    a_model = sentence_bert_model.encode(answer_list)
    np.save('../model/q_embedding.npy', q_model)
    np.save('../model/a_embedding.npy', a_model)


datapath = './data/data_final.csv'
data_frame = get_dataframe(datapath)
process_embedding(data_frame)

# training model
#question_list, answer_list = get_list(data_frame)

#train_data = [InputExample(texts=question_list, label=0.8),InputExample(texts=answer_list, label=0.7)]
#train_dataloader = DataLoader(train_data, shuffle=True, batch_size=16)
#train_loss = losses.CosineSimilarityLoss(sentence_bert_model)
#sentence_bert_model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=1, warmup_steps=100)
#torch.save(train_dataloader, './model/train_model')
