#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup


# In[2]:


from urllib.request import urlopen


# In[3]:


url  = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')
html


# In[6]:


soup = BeautifulSoup(html,'html.parser') # bs object assigned to variable called soup
                                         # Arguments are "html" a variable to be parsed, and 
                                         # "html.parser" its a string tells soup object to parse the html page 
                                         #  "html.parser"  is a python's buit-in-HTMLparser


# In[7]:


soup


# In[9]:


# get_text() method to extact text from the soup


# In[24]:


soup.get_text()


# ##### Here you you will encouter with blank or escape charecters to remove this we use .replace() method

# In[25]:


soup.get_text().replace("\n", " ")


# #### Now we are fetching instance of  img tag  using find() and find_all()

# In[27]:


soup.find_all("img")


# this has returned the tag objects of list caontaing available image tag in the html page   
# so first we need to unpack these returned list into single object

# In[28]:


img1, img2 = soup.find_all("img")


# In[29]:


img1


# In[30]:


img2


# to access the src attribute use dectionary notation

# In[32]:


img1["src"]


# In[37]:


soup.title  # HTML documents can be accessed by properties of the Tag object.


# In[38]:


soup.title.string


# One of the features of Beautiful Soup is the ability to search for specific kinds of tags whose attributes match certain values.

# In[41]:


soup.find_all("img", src="/static/dionysus.jpg")


# Example 1

# In[46]:


url = "http://olympus.realpython.org/profiles"


# In[49]:


page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")
soup


# In[50]:


soup.find_all("a")


# In[63]:


a1,a2,a3 = soup.find_all("a")


# In[65]:


for link in soup.find_all("a"):
    link_url = url + link["href"]
    print(link_url)


# 
# # Documentation Practice

# In[1]:


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# In[4]:


soup  = BeautifulSoup(html_doc, "html.parser")


# In[6]:


soup.prettify()


# In[7]:


soup.title


# In[8]:


soup.title.name


# In[9]:


soup.title.string


# In[10]:


soup.title.parent


# In[11]:


soup.p


# In[13]:


soup.p["class"]


# In[14]:


soup.find("a")


# In[15]:


soup.find_all("a")


# In[20]:


soup.find(id="link3")


# One common task is extracting all the URLs found within a page’s <a> tags:

# In[25]:


for link in soup.find_all("a"):
    print(link.get('href'))


# In[26]:


# all text from page


# In[29]:


soup.get_text()


# To parse documents

# In[31]:


# with open("index.html") as fb:
#     soup = BeautifulSoup(fb)
# soup = BeautifulSoup('<html>data</html>')


# Kinds of objects  
# Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. But you’ll only ever have to deal with about  
# four kinds of objects: Tag, NavigableString, BeautifulSoup, and Comment.

# In[32]:


soup = BeautifulSoup('<b class="boldest">Extremly Bold</b>')


# In[35]:


tag =soup.b
tag


# In[36]:


tag.name


# In[37]:


type(tag)


# Changing the tag's feature 1) name 
# ####  1) Name

# In[38]:


tag.name = "boldqoute"
tag


# In[39]:


tag.name


# #### 2) Attribute

# In[40]:


# attribute is class, id


# In[41]:


tag['class']


# In[42]:


tag.attrs


# You can add, remove, and modify a tag’s attributes. Again, this is done by treating the tag as a dictionary:

# #### ADD

# In[51]:


tag['class'] = 'very bold'
tag['another-attribute'] = 1
tag['id'] = 'bold-epic'
tag


# #### DELETE

# In[52]:


del tag['id']


# In[61]:


tag.attrs


# In[65]:


tag.string
type(tag.string)


# In[67]:


tag.string.replace_with('NO Bold ')
tag.string
tag


# #### Multivalued Attribute

# multi-Valued attribute is class in HtML5  
# tag can have many css class

# In[60]:


css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']


# In[ ]:




