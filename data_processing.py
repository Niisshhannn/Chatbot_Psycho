import pandas as pd

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