import server.default_msg as defmsg
from server.communication import communicate
import server.default_opt as defopt
from server.joke import get_joke

# return a sentence according to language and type and what we say


def chat(msg, lang, typ):
    '''
    explication des paramètres:
        msg : message de client
        lang: la langue choisie  / valeur peut être vide
        typ : le type choise / valeur peut être vide
    valeur retourné      : retrouner un dictionnaire
        msg    : parole de chatbot
        options: les options pour les clients / les valeurs peut être vide
    '''
    ret_msg = ''
    ret_opt = []
    # commencement du dialogue

    def judge_lang(a_dict: dict):
        return a_dict[lang] if a_dict[lang] else a_dict['en']

    if msg == '#init':
        ret_msg = defmsg.MSG_WELCOME
        ret_opt = defopt.OPTIONS_LANG
    # feedback après avoir choisi la langue
    elif msg == '#lang':
        ret_msg = judge_lang(defmsg.MSG_FEEDBACK_WELCOME_DICT)
        ret_opt = judge_lang(defopt.OPTIONS_TYPE_DICT)
    # feedback après avoir choisi le type
    elif msg == '#type':
        if typ in ['psy', 'drug', 'others']:
            ret_msg = judge_lang(defmsg.MSG_FEEDBACK_QUESTION_DICT)
        elif typ == 'joke':
            ret_msg = 'a joke'
            ret_opt = judge_lang(defopt.OPTION_RETURN_JOKE_DICT)
        elif typ == 'back_lang':
            ret_msg = defmsg.MSG_RE_WELCOME
            ret_opt = defopt.OPTIONS_LANG
        elif typ == 'back_type':
            ret_msg = judge_lang(defmsg.MSG_FEEDBACK_WELCOME_DICT)
            ret_opt = judge_lang(defopt.OPTIONS_TYPE_DICT)
    # feedback bye
    else:
        bye = ['Au revoir', '再见', 'Bye', '拜拜', 'bye',
               'byebye', 'au revoir', 'salut', 'Salut']
        emm = ['emmmmm', 'emm', 'emmm', 'emmmm', 'euh', '呃', 'Euh']
        tks = ['谢谢', 'merci', 'Merci', 'Merci beaucoup', 'merci beaucoup',
               'Thanks', 'Thank you so much', 'thanks', 'thank you so much']
        if msg in bye:
            ret_msg = judge_lang(defmsg.MSG_BYE_DICT)
        elif msg in emm:
            ret_msg = judge_lang(defmsg.MSG_FEEDBACK_EMM_DICT)
        elif msg in tks:
            ret_msg = judge_lang(defmsg.MSG_FEEDBACK_TKS_DICT)
        else:
            ret_msg = communicate(msg, lang, typ)

    if len(ret_opt) == 0:
        ret_opt = judge_lang(defopt.OPTION_RETURN_DICT)

    return {'msg': ret_msg, 'options': ret_opt}
