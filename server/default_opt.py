# option défini


OPTIONS_LANG = [{'key': 'fr', 'value': 'Français'},
                {'key': 'zh', 'value': '中文'},
                {'key': 'en', 'value': 'English'}]


OPTIONS_TYPE_DICT = {
    'zh': [{'key': 'psy', 'value': '心理咨询'},
           {'key': 'drug', 'value': '药物咨询'},
           {'key': 'others', 'value': '其他问题'}],
    'fr': [{'key': 'psy', 'value': 'Psychologie'},
           {'key': 'drug', 'value': 'Drogue'},
           {'key': 'others', 'value': 'Autres'},
           {'key': 'joke', 'value': 'Blagues'}],
    'en': [{'key': 'psy', 'value': 'Psychology'},
           {'key': 'drug', 'value': 'Drug'},
           {'key': 'others', 'value': 'Others'},
           {'key': 'joke', 'value': 'Jokes'}]
}

OPTION_RETURN_DICT = {
    'zh': [{'key': 'back_lang', 'value': '更换语言'},
           {'key': 'back_type', 'value': '更换类型'}],
    'fr': [{'key': 'back_lang', 'value': 'Changer la langue'},
           {'key': 'back_type', 'value': 'Changer le type'}],
    'en': [{'key': 'back_lang', 'value': 'Change language'},
           {'key': 'back_type', 'value': 'Change type'}]
}

OPTION_RETURN_JOKE_DICT = {
    'fr': [{'key': 'back_lang', 'value': 'Changer la langue'},
           {'key': 'back_type', 'value': 'Changer le type'},
           {'key': 'joke', 'value': 'Une blague de plus'}],
    'en': [{'key': 'back_lang', 'value': 'Change language'},
           {'key': 'back_type', 'value': 'Change type'},
           {'key': 'joke', 'value': 'One more joke'}]
}
