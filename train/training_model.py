from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

#sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')
#sentence_bert_model = SentenceTransformer('paraphrase-distilroberta-base-v1')
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


datapath = '../data/data_final.csv'
data_frame = get_dataframe(datapath)
process_embedding(data_frame)
