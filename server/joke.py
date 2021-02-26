import pandas as pd
import random

def get_joke(lang):
    if lang == 'fr':
        joke= pd.read_csv('./data/joke_fr.csv',sep=';',names=['Joke'])
    elif lang == 'en':
        joke = pd.read_csv('./data/joke_en.csv',sep=';',names=['Joke'])
    joke_list = joke['Joke'].to_list()
    joke_sample = random.choice(joke_list)
    return joke_sample
