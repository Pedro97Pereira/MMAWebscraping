from bs4 import BeautifulSoup
import requests 
import pandas as pd
import seaborn as sb 
import numpy as np

#Import  from Wikipedia

results_event_url = 'https://en.wikipedia.org/wiki/UFC_274'

request_event = requests.get(results_event_url)

#parse html

list_event_soup = BeautifulSoup(request_event.content, 'html.parser')

#find table

list_event_table_soup = list_event_soup.find('table', {'class': 'toccolours'})

#table to dataframe

df_list_event_soup = pd.read_html(str(list_event_table_soup))

df_event_soup = pd.DataFrame(df_list_event_soup[0])

#remove multyindex, useless row 

df_event_soup = df_event_soup.droplevel(level=0, axis=1)

#clean the data

prelims = ['Early', 'Preliminary']

eventColumns = ['Weight class', 'Winner', 'Action', 'Loser', 'Method', 'Round', 'Time', 'Notes']

df_event_soup.columns = eventColumns 

df_event_soup = df_event_soup[df_event_soup['Winner'].str.contains('|'.join(prelims))==False]

#export to csv

df_event_soup.to_csv('df_event_soup.csv', encoding='utf-8')


