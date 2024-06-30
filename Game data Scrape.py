#!/usr/bin/env python
# coding: utf-8

# ## Web Scracpping : Zulrah Game

# In[1]:


# import libraries


# In[5]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


# Grab Data from page

# In[43]:


# Store the url in variable

url = 'https://oldschool.runescape.wiki/w/Zulrah'

# get the response of the website to access the content

response = requests.get(url, headers = {'User-Agent': 'Google-Chrome'})

# extract html from response
page = response.content

#parse Html
soup = BeautifulSoup(page, 'lxml')

# extarct all  tables in html
drop_tables = soup.find_all('table', attrs= {'class': 'wikitable sortable filterable item-drops autosort=4,a'})

# initialize empty dictionary to combine all the  
loot_tables = {}
table_index = 0

# iterate through table and parse them individualy
for table in drop_tables:
    # parse out table rows
    table_rows = table.find_all('tr')
    
    # parse out table headers
    table_header = table.find_all('th')
    
    # parse out columns from table header
    cols = []
    for item in table_header:
        if len(item.text)>0:
            cols.append(item.text)
            
    # parse data each rows
    data = []
    for row in table_rows:
        table_data = row.find_all('td')
        # parse out table data list 
        row_data = [item.text for item in table_data if item.text != '']
        
        # removes blank data
        if len(row_data) >0:
            data.append(row_data) 
            
    # putting in a frame
    output_dataframe  = pd.DataFrame(data, columns = cols)
    
    # set dictionary table as default table
    loot_tables.setdefault(table_index, output_dataframe)
    
    # each time run through increement by 1
    table_index += 1
    
# join all the tables into one
loot_table= pd.concat(loot_tables.values())

# set index as Items of list
loot_table.set_index('Item', inplace=True)    

# output
loot_table


# In[ ]:




