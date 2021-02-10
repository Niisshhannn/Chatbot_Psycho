from sentence_transformers import SentenceTransformer
from google_trans_new import google_translator
import numpy as np
import pandas as pd

sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')
translator = google_translator()


def get_data(path):
    psycho_frame = pd.read_csv(path, sep=';', names=['Question', 'Reponse'])
    return psycho_frame


def get_list(path_input):
    psycho_frame = get_data(path_input)
    question_list = psycho_frame['Question'].to_list()
    reponse_list = psycho_frame['Reponse'].to_list()
    return question_list, reponse_list


def process_embedding(path_input):
    question_list, reponse_list = get_list(path_input)
    question_embedding = sentence_bert_model.encode(question_list)
    reponse_embedding = sentence_bert_model.encode(reponse_list)


def cosine_similarity(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


def get_similarity_max(vector_a, liste):
    sim_list = []
    for ele in liste:
        sim = cosine_similarity(vector_a, sentence_bert_model.encode([ele])[0])
        sim_list.append(sim)
    max = max(sim_list)
    idx = sim_list.index(max)
    return max, idx


def welcome_bot():
    content = 'BOT : Hello, I am a baby of mom Shanshan and dad Cancan, I can speak French, Chinese and English, what language do you speak? Please input en or ch or fr "'
    return content


def feedback_welcome():
    language = input()
    if language == 'fr':
        return "BOT: D'accord, qu'est-ce que je peux vous aider ?"
    if language == 'zh':
        return "BOT: 好的，请问有什么可以帮助您的呢？"
    if language == 'en':
        return "BOT: Okay, what can I help you with?"


def get_reponse(query_vect, question_list, reponse_list):
    sim_query_question_max, idx_qq = get_similarity_max(
        query_vect, question_list)
    sim_query_reponse_max, idx_qr = get_similarity_max(
        query_vect, reponse_list)
    if sim_query_question_max < sim_query_reponse_max:
        return reponse_list[idx_qq]
    else:
        return reponse_list[idx_qr]


def communication(query):
    query_language = translator.detect(query)
    query_en = translator.translate(
        query, lang_src=query_language, lang_tgt='en')
    query_vect = sentence_bert_model.encode([query_en])[0]
    reponse = get_reponse(query_vect, question_list, reponse_list)
    reponse_translate = translator.translate(
        reponse, lang_src='en', lang_tgt=query_language)
    feedback = "BOT: " + reponse_translate
    return feedback


def bye_feedback():
    return 'Bye'

def chatbot():

    welcome_bot()
    feedback_welcome()

    datapath = 'data/Q_R_en.csv'
    question_list, reponse_list = get_list(datapath)
    process_embedding(datapath)

    while True:
        try:
            query = input('You : ')
            if 'bye' in query:
                bye_feedback()
                break
            else:
                communication(query)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == '__main__':
    chatbot()