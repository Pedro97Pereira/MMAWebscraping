
from bs4 import BeautifulSoup
import requests 
import pandas as pd
import seaborn as sb 
import numpy as np

#Este ficheiro tem a base do webscraping mas para uma tabela à qual eu vou buscar as paginas dos eventos

list_of_ufc_events_url = 'https://en.wikipedia.org/wiki/List_of_UFC_events'

request_list_ufc = requests.get(list_of_ufc_events_url)

id_table_list_ufc = 'Past_events'

"""
#save the html page locally
def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)
        
        
save_html(request_list_ufc.content, 'List_of_UFC_events')

#Open html file
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
    
    
html = open_html('List_of_UFC_events')
"""
#parse html file with beautiful soup

list_ufc_soup = BeautifulSoup(request_list_ufc.text, 'html.parser')

list_ufc_table_soup = list_ufc_soup.find('table', attrs={'id': id_table_list_ufc})

df_list_ufc_soup = pd.read_html(str(list_ufc_table_soup))

print(df_list_ufc_soup)

