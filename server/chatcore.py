import server.default_msg as defmsg
from server.communication import communicate


def joke(lang):
    pass


OPTIONS_LANG = [{'key': 'fr', 'value': 'Français'},
                {'key': 'zh', 'value': '中文'},
                {'key': 'en', 'value': 'English'}]
OPTIONS_TYPE_CH = [{'key': 'psy', 'value': '心理咨询'},
                   {'key': 'drug', 'value': '药物咨询'},
                   {'key': 'others', 'value': '其他问题'}]
OPTIONS_TYPE_FR = [{'key': 'psy', 'value': 'Psychologie'},
                   {'key': 'drug', 'value': 'Drogue'},
                   {'key': 'others', 'value': 'Autres'}]
OPTIONS_TYPE_EN = [{'key': 'psy', 'value': 'Psychology'},
                   {'key': 'drug', 'value': 'Drug'},
                   {'key': 'others', 'value': 'Others'}]


# retourner la réponse selon le choix de la langue et le type de client
def chat(msg, lang, typ):
    '''
    参数说明:
        msg : 用户说的话
        lang: 对应的语言       / 值可为空
        typ : 选了哪个类型的对话 / 值可为空
    返回值      : 返回字典
        msg    : chatbot说的话
        options: 可以给用户的选项 / 值可以为空
    '''
    ret_msg = ''
    ret_opt = []
    # le commencement de dialogue
    if msg == '#init':
        ret_msg = defmsg.MSG_WELCOME
        ret_opt = OPTIONS_LANG
    # feedback après avoir choisi la langue
    elif msg == '#lang':
        if lang == 'zh':
            ret_msg = defmsg.MSG_FEEDBACK_WELCOME_CH
            ret_opt = OPTIONS_TYPE_CH
        elif lang == 'fr':
            ret_msg = defmsg.MSG_FEEDBACK_WELCOME_FR
            ret_opt = OPTIONS_TYPE_FR
        else:
            ret_msg = defmsg.MSG_FEEDBACK_WELCOME_EN
            ret_opt = OPTIONS_TYPE_EN
    # feedback après avoir choisi le type
    elif msg == '#type':
        if lang == 'zh':
            ret_msg = defmsg.MSG_FEEDBACK_QUESTION_CH
        elif lang == 'fr':
            ret_msg = defmsg.MSG_FEEDBACK_QUESTION_FR
        else:
            ret_msg = defmsg.MSG_FEEDBACK_QUESTION_EN
    # feedback bye
    else:
        bye = ['Au revoir', '再见', 'Bye', '拜拜', 'bye', 'byebye','au revoir','salut']
        if msg in bye:
            if lang == 'zh':
                ret_msg = defmsg.MSG_BYE_CH
            elif lang == 'fr':
                ret_msg = defmsg.MSG_BYE_FR
            else:
                ret_msg = defmsg.MSG_BYE_EN
        else:
            ret_msg = communicate(msg, lang, typ)

    return {'msg': ret_msg, 'options': ret_opt}
