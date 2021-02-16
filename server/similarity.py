from sentence_transformers import SentenceTransformer, util

sentence_bert_model = SentenceTransformer('bert-base-nli-mean-tokens')


def get_cosin_sim(vector_a, vector_b):
    return util.pytorch_cos_sim(vector_a, vector_b)


def cos_sim(vector_a, vector_b):
    return util.pytorch_cos_sim(vector_a, vector_b)

# obtenir la similarité maximun
def get_similarity_max(vector_a, liste):
    sim_list = []
    for ele in liste:
        sim = get_cosin_sim(vector_a, sentence_bert_model.encode([ele])[0])
        sim_list.append(sim)
    max_sim = max(sim_list)
    idx = sim_list.index(max_sim)
    return max_sim, idx


def get_answer(query_vect, question_list, answer_list):
    sim_query_question_max, idx_qq = get_similarity_max(
        query_vect, question_list)
    sim_query_answer_max, idx_qr = get_similarity_max(
        query_vect, answer_list)
    if sim_query_question_max < sim_query_answer_max:
        return answer_list[idx_qq]
    else:
        return answer_list[idx_qr]

# converti une phrase vers le vectors
def get_embedding(sentence):
    vec = sentence_bert_model.encode([sentence])[0]
    return vec
