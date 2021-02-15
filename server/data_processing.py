import pandas as pd


def get_dataframe(path):
    df = pd.read_csv(path, sep=';', names=['Question', 'Type', 'Answer'])
    return df


def get_list(df):
    question_list = df['Question'].to_list()
    answer_list = df['Answer'].to_list()
    return question_list, answer_list
