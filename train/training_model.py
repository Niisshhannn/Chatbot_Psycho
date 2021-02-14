from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

#sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')
#sentence_bert_model = SentenceTransformer('paraphrase-distilroberta-base-v1')
sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')

def get_dataframe(path):
    df = pd.read_csv(path, sep=';', names=['Question', 'Type', 'Answer'])
    return df

def get_list(df):
    question_list = df['Question'].to_list()
    answer_list = df['Answer'].to_list()
    return question_list, answer_list

# transfer sentence to vector

def process_embedding(df):
    question_list, answer_list = get_list(df)
    answer_list = [str(i) for i in answer_list]
    sentence_bert_model.encode(question_list)
    sentence_bert_model.encode(answer_list)
    #sentence_bert_model.save(output_path="model/embedding_train")
    np.save('model/embedding.npy',sentence_bert_model)


datapath = './data/data_final.csv'
data_frame = get_dataframe(datapath)
process_embedding(data_frame)

