#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"


# In[4]:


page = requests.get(url)

soup = BeautifulSoup(page.text,"html.parser")


# In[5]:


soup


# In[6]:


soup.find('table')


# In[7]:


soup.find_all('table')[1]


# In[8]:


soup.find('table', class_ ="wikitable sortable")


# In[9]:


table=soup.find_all('table')[1]


# In[10]:


print(table)


# In[11]:


#pulling out th title tags ie table headers

world_titles = table.find_all("th")


# In[12]:


#now we are doing list compherension to get the titles
world_titles


# In[13]:


World_table_titles = [title.text.strip() for title in world_titles]
print(World_table_titles)


# In[14]:


import pandas as pd


# In[27]:


df = pd.DataFrame(columns = World_table_titles)
df


# In[17]:


column_data = table.find_all("tr")


# In[28]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_data 


# In[29]:


print(individual_data)


# In[30]:


df


# In[ ]:




