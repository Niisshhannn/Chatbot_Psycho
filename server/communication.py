import pandas as pd
import numpy as np
from server.similarity import get_embedding, cos_sim
from server.translator import get_translate_en, get_translate_lang


def get_df():
    path = './data/data_final.csv'
    df = pd.read_csv(path, sep=';')
    q_vec_list = np.load('./model/q_embedding.npy')
    a_vec_list = np.load('./model/a_embedding.npy')
    q_df = pd.DataFrame(q_vec_list)
    a_df = pd.DataFrame(a_vec_list)
    return df, q_df, a_df


# obtenir trois dataframes
df, q_df, a_df = get_df()

# pour trouver les réponses correspondants
def get_ans(msg, typ):
    dfloc = df[df['Type'] == typ]
    all_index = dfloc.index
    q_dfloc = q_df.loc[all_index]
    a_dfloc = a_df.loc[all_index]
    msg_vec = get_embedding(msg)
    max_sim = 0
    max_idx = None
    for idx, vec in q_dfloc.iterrows():
        sim = cos_sim(msg_vec, vec)
        if sim > max_sim:
            max_sim = sim
            max_idx = idx
    for idx, vec in a_dfloc.iterrows():
        sim = cos_sim(msg_vec, vec)
        if sim > max_sim:
            max_sim = sim
            max_idx = idx
    if max_idx is None:
        return None
    return df.loc[max_idx]['Answer']

# retourner la réponse
def core_fin(msg, typ):
    answer = get_ans(msg, typ)
    if answer is None or (answer != 'No answer' and answer != 'Unanswerable'):
        return answer
    return "Sorry, I can't answer this question, but I will try hard to learn it. ^_^ "

# communication
def communicate(msg, lang, typ):
    if lang == 'en':
        return core_fin(msg, typ)
    msg_en = get_translate_en(msg, lang)
    answer_en = core_fin(msg_en, typ)
    answer = get_translate_lang(answer_en, lang)
    return answer
