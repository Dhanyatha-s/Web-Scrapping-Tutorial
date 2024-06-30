#!/usr/bin/env python
# coding: utf-8

# ## TOP RATED  IMDB MOVIES NAMES

# In[78]:


import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


# Grab Data from Website

# In[79]:


url = 'https://www.imdb.com/chart/top'


# In[80]:


response = requests.get(url, headers={'User-Agent': 'Google-Chrome'})


# In[81]:


response


# In[82]:


# extarct html from resopnse
page = response.content
#page


# In[83]:


# parse Html
soup = BeautifulSoup(page, 'lxml')
#soup.prettify()


# In[84]:


# data is in the un-ordered list
# find all the ul from the wesite
unorderd_list = soup.find_all('ul', attrs={'class':'ipc-metadata-list'})


# In[85]:


# for list in unorderd_list:
    
#     li = list.find_all('li')
    
#     #find the div tag from li
    
#     for div in li:
#         summary = div.find_all('div', attrs={'class':'sc-b189961a-0 hBZnfJ cli-children'})
        
#     for title in summary:
#         movie_title = title.find_all('a')
#         for header in movie_title:
#             name = header.find_all('h3', attrs= {'class':'ipc-title__text'})
#             for t in name:
#                 text = t.text
#                 print(text)


# In[87]:


unorderd_list = soup.find_all('ul', attrs={'class':'ipc-metadata-list'})
for ul in unorderd_list:
    lists= ul.find_all('li')
    for summary in lists:
        data_container = summary.find_all('div',attrs={'class':'ipc-metadata-list-summary-item__tc'})
        for title in data_container:
            movie_title = title.find_all('a')
            for header in movie_title:
                name = header.find_all('h3', attrs= {'class':'ipc-title__text'})
                for t in name:
                    text = t.text
                    print(text)


# In[98]:


unorderd_list = soup.find_all('ul', attrs={'class':'ipc-metadata-list'})
for ul in unorderd_list:
    li = ul.find_all('li', attrs= "ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")
    for text in li:
        movie_name = text.get_text()


# In[99]:


movie_name


# In[ ]:




