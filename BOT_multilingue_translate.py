from google_trans_new import google_translator
from sentence_transformers import SentenceTransformer, util
#from scipy.spatial.distance import cosine
from training_model import get_dataframe, get_list
import numpy as np

translator = google_translator()
#sentence_bert_model = np.load('model/embedding.npy')
sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')


def classify_data(df):
    psycho_frame = df[df['Type'] == 'psychology']
    other_frame = df[df['Type'] == 'not_drug_question']
    drug_frame = df[(df['Type'] != 'psychology') & (
        df['Type'] != 'not_drug_question')]
    return psycho_frame, other_frame, drug_frame

# calculate similarity between two vectors


def cosine_similarity(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


def get_cosin_sim(vector_a, vector_b):
    #sim = 1 - cosine(vector_a, vector_b)
    return util.pytorch_cos_sim(vector_a, vector_b)


# get the biggest similarity and its index in a list of sentence


def get_similarity_max(vector_a, liste):
    sim_list = []
    for ele in liste:
        #sim = cosine_similarity(vector_a, sentence_bert_model.encode([ele])[0])
        sim = get_cosin_sim(vector_a, sentence_bert_model.encode([ele])[0])
        sim_list.append(sim)
    max_sim = max(sim_list)
    idx = sim_list.index(max_sim)
    return max_sim, idx


def welcome_bot():
    content = "Hello, my name is Melody, I'm the baby of mom Shanshan and dad Cancan, I can speak French, Chinese and English, what language do you speak? Please input en or ch or fr "
    print("BOT: ", content)
    # return content


def feedback_welcome(language):
    if language == 'fr':
        print("BOT : D'accord, qu'est-ce que je peux vous aider ? ")
        # return "D'accord, qu'est-ce que je peux vous aider ? "
    if language == 'zh':
        print("BOT : 好的，请问有什么可以帮助您的呢？")
        # return "好的，请问有什么可以帮助您的呢？"
    if language == 'en':
        print("BOT : Okay, what can I help you with ? ")
        # return "Okay, what can I help you with ? "


def feedback_bye():
    print('BOT : Bye ! Have a nice day !')
    # return 'Bye ! Have a nice day !'

# three buttons to classify questions


def type_choix(psy_df, other_df, drug_df):
    print('select your type for consulting : psychology, drug, others')
    type_ch = input()
    print('YOU : ', type_ch)
    if type_ch == 'psychology':
        question_list, answer_list = get_list(psy_df)
        print('now you can entrer your questions.')
        return question_list, answer_list
    if type_ch == 'others':
        question_list, answer_list = get_list(other_df)
        print('now you can entrer your questions.')
        return question_list, answer_list
    if type_ch == 'drug':
        question_list, answer_list = get_list(drug_df)
        print('now you can entrer your questions.')
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


def communication(language, query, question_list, answer_list):
    if not language == 'en':
        query_en = translator.translate(
            query, lang_src=language, lang_tgt='en')
        query_vect = sentence_bert_model.encode([query_en])[0]
        answer = get_answer(query_vect, question_list, answer_list)
        if not answer == 'No answer' or 'Unanswerable':
            answer_translate = translator.translate(
                answer, lang_src='en', lang_tgt=language)
            print(answer_translate)
        else:
            print(
                "BOT : Sorry, I don't know how to answer this question, but I will try hard to learn it.")
    else:
        query_vect = sentence_bert_model.encode([query])[0]
        answer = get_answer(query_vect, question_list, answer_list)
        if not answer == 'No answer' or 'Unanswerable':
            print(
                "BOT : Sorry, I don't know how to answer this question, but I will try hard to learn it.")
        else:
            print(answer)
    # return "Sorry, I don't know how to answer this question, but I will try hard to learn it."
    # return answer_translate


def chatbot():

    datapath = 'data/data_final.csv'
    data_frame = get_dataframe(datapath)

    psycho_frame, other_frame, drug_frame = classify_data(data_frame)

    welcome_bot()
    language = input()
    feedback_welcome(language)

    question_list, answer_list = type_choix(
        psycho_frame, other_frame, drug_frame)

    while True:
        try:
            query = input()
            if 'bye' in query:
                feedback_bye()
                break
            else:
                communication(language, query, question_list, answer_list)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == '__main__':
    chatbot()
