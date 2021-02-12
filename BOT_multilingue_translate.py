from sentence_transformers import SentenceTransformer
from google_trans_new import google_translator
import numpy as np
import pandas as pd

sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')
#sentence_bert_model = SentenceTransformer('paraphrase-distilroberta-base-v1')
translator = google_translator()

# data process


def get_dataframe(path):
    df = pd.read_csv(path, sep=';', names=['Question', 'Type', 'Answer'])
    return df


def classify_data(df):
    psycho_frame = df[df['Type'] == 'psychology']
    other_frame = df[df['Type'] == 'not_drug_question']
    drug_frame = df[(df['Type'] != 'psychology') & (
        df['Type'] != 'not_drug_question')]
    return psycho_frame, other_frame, drug_frame


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


# calculate similarity between two vectors
def cosine_similarity(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


# get the biggest similarity and its index in a list of sentence
def get_similarity_max(vector_a, liste):
    sim_list = []
    for ele in liste:
        sim = cosine_similarity(vector_a, sentence_bert_model.encode([ele])[0])
        sim_list.append(sim)
    max_sim = max(sim_list)
    idx = sim_list.index(max_sim)
    return max_sim, idx


def welcome_bot():
    content = 'Hello, I am a baby of mom Shanshan and dad Cancan, I can speak French, Chinese and English, what language do you speak? Please input en or ch or fr '
    return content


def feedback_welcome():
    language = input()
    if language == 'fr':
        return "D'accord, qu'est-ce que je peux vous aider ? "
    if language == 'zh':
        return "好的，请问有什么可以帮助您的呢？"
    if language == 'en':
        return "Okay, what can I help you with ? "


def feedback_bye():
    return 'Bye'

# three buttons to classify questions


def type_choix(psy_df, other_df, drug_df):
    type_ch = input()
    if type_ch == 'psychology':
        question_list, answer_list = get_list(psy_df)
        return question_list, answer_list
    if type_ch == 'others':
        question_list, answer_list = get_list(other_df)
        return question_list, answer_list
    if type_ch == 'drug':
        question_list, answer_list = get_list(drug_df)
        return question_list, answer_list


def get_answer(query_vect, question_list, answer_list):
    sim_query_question_max, idx_qq = get_similarity_max(
        query_vect, question_list)
    sim_query_answer_max, idx_qr = get_similarity_max(
        query_vect, answer_list)
    if sim_query_question_max < sim_query_answer_max:
        return answer_list[idx_qq]
    else:
        return answer_list[idx_qr]


def communication(query, question_list, answer_list):
    query_language = translator.detect(query)
    query_en = translator.translate(
        query, lang_src=query_language, lang_tgt='en')
    query_vect = sentence_bert_model.encode([query_en])[0]
    answer = get_answer(query_vect, question_list, answer_list)
    if answer == 'No answer' or 'Unanswerable' or '':
        return "Sorry, I don't know how to answer this question, but I will try hard to learn it."
    else:
        answer_translate = translator.translate(
            answer, lang_src='en', lang_tgt=query_language)
        return answer_translate


def chatbot():

    datapath = 'data/data_final.csv'
    data_frame = get_dataframe(datapath)

    process_embedding(data_frame)
    psycho_frame, other_frame, drug_frame = classify_data(data_frame)

    welcome_bot()
    feedback_welcome()

    question_list, answer_list = type_choix(
        psycho_frame, other_frame, drug_frame)

    while True:
        try:
            query = input()
            if 'bye' in query:
                feedback_bye()
                break
            else:
                communication(query, question_list, answer_list)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == '__main__':
    chatbot()
