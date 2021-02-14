import pandas as pd
import json

# read data excel
data_excel = pd.read_excel('data/MedInfo2019-QA-Medications.xlsx',header=0)

# process data excel
type_label = set(data_excel['Question Type'].to_list())
data = data_excel[['Question','Question Type','Answer']]
data.rename(columns={'Question':'Question','Question Type':'Type','Answer':'Answer'},inplace=True)

# processe data pyschology
data_psy = pd.read_csv('data/Q_R_en.csv',sep=';',names=['Question','Answer'])
psy_lable_list = ['psychology']*len(data_psy)
psy_lable_frame = pd.DataFrame(psy_lable_list,columns=['Type'])
data_psy_update = pd.concat([data_psy,psy_lable_frame],axis=1,ignore_index=False)
data_psy_update = data_psy_update[['Question','Type','Answer']]

# merge two dataset
data_total = pd.concat([data,data_psy_update],axis=0,ignore_index=False)
#data_total = data_total[~data_total['Answer'].isin(['No answers'])]
data_total.to_csv('data/data_final.csv',header=True,index=False,sep=';')

# process joke data 
def load_json(path):
    file = open(path,'r',encoding='utf-8')
    data = json.load(file)
    return data

# data - en
joke_en_data = load_json('data/joke_en.json')

en_body = []
en_title = []
for i in range(len(joke_en_data)-1):
    en_body.append(joke_en_data[i]['body'])
    en_title.append(joke_en_data[i]['title'])

# to dataframe
en_title_frame = pd.DataFrame(en_title,columns=['Joke'])
en_body_frame =  pd.DataFrame(en_body,columns=['Answer'])
joke_en_df = pd.concat([en_title_frame,en_body_frame],axis=1,ignore_index=False)

joke_en_df.to_csv('data/joke_en.csv',sep=';',header=True,index=False)

# data - fr
joke_fr_data = load_json('data/json_fr.json')

fr_joke = []
fr_answer = []
for j in range(len(joke_fr_data)-1):
    fr_joke.append(joke_fr_data[j]['joke'])
    fr_answer.append(joke_fr_data[j]['answer'])

fr_joke_frame = pd.DataFrame(fr_joke,columns=['Joke'])
fr_answer_frame = pd.DataFrame(fr_answer,columns=['Answer'])
joke_fr_df = pd.concat([fr_joke_frame,fr_answer_frame],axis=1,ignore_index=False)

joke_fr_df.to_csv('data/joke_fr.csv',sep=';',header=True, index=False)
