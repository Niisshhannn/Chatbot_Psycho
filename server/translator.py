from google_trans_new import google_translator
translator = google_translator()

# phase de traduction automatique entre les langues différentes
def get_translate_en(msg, lang):
    msg_trans = translator.translate(msg, lang_src=lang, lang_tgt='en')
    return msg_trans


def get_translate_lang(msg, lang):
    msg_en = translator.translate(msg, lang_src='en', lang_tgt=lang)
    return msg_en
