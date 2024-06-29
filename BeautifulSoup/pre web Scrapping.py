#!/usr/bin/env python
# coding: utf-8

# # Web Scrapping

# Scarp Web Page

# In[1]:


# using urllib library
# it has a method called urllib.request
###### it has a function called urlopen() ---> returns HTTPResponse Object
########## with this opened we are going to read() it ---> parsed with HTTPResponse Object


# In[27]:


from  urllib.request import urlopen


# In[28]:


url = "http://olympus.realpython.org/profiles/aphrodite"


# In[29]:


page = urlopen(url)


# In[30]:


page


# In[31]:


html_bytes = page.read()


# In[60]:


html = html_bytes.decode('utf-8')


# In[33]:


html


# Text Extraction

# In[35]:


title_index = html.find("<title>")
title_index


# In[38]:


start_Index = title_index + len('<title>')
start_Index


# In[39]:


end_index = html.find("</title>")
end_index


# In[40]:


title = html[start_Index:end_index]
title


# Example 2

# In[41]:


url = "http://olympus.realpython.org/profiles/poseidon"


# In[49]:


page = urlopen(url)
html_byte = page.read()
html = html_byte.decode('utf-8')
html


# In[53]:


start_index = html.find("<title>") + len("<title>")
end_index   = html.find("</title>")
title       = html[start_index:end_index]
title


# In[ ]:





# Example 3 GfG page 

# In[32]:


from bs4 import BeautifulSoup
url = 'https://www.geeksforgeeks.org/web-pages/'


# In[33]:


page = urlopen(url)


# In[34]:


html_byte = page.read()


# In[35]:


html = html_byte.decode('utf-8') 


# In[37]:


soup = BeautifulSoup(html, "html.parser")
soup


# In[59]:


start_index = html.find('<title>') + len('<title>')
end_index = html.find('</title>')
title = html[start_index:end_index]
title


# Example 4

# In[22]:


url = 'https://ashutoshhathidara.com'


# In[23]:


page = urlopen(url)


# In[24]:


html_byte = page.read()


# In[26]:


html = html_byte.decode()
html


# Exmaple 5

# In[13]:


url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html=page.read().decode('utf-8')
html


# In[31]:


for string in ["Name:", "Favorite Color:"]:
    ft_indx = html.find(string)
    #print(string)
    text_indx = ft_indx + len(string)
    #print(text_indx)
    
    nx_indx_offset = html[text_indx:].find("<")
    end_indx = text_indx + nx_indx_offset
    #print(end_indx)
    raw_text = html[text_indx:end_indx]
    #print(raw_text)
    text = raw_text.strip('\r\n\t')
    print(text)
    


# In[29]:





# In[ ]:





# In[ ]:





# # Regular expression
# 

# In[3]:


import re
import requests


# In[2]:


from urllib.request import urlopen


# In[7]:


url = "http://olympus.realpython.org/profiles/dionysus"
response =requests.get(url) 
page = urlopen(url)
html = page.read().decode("utf-8")
html


# In[9]:


pattern = '<title.*?>.*?</title.*?>'
match = re.search(pattern, html,re.IGNORECASE)
title_match = match.group()
title_match


# In[11]:


title = re.sub("<.*?>","",title_match)
title


# In[ ]:




