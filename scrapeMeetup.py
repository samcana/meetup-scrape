#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


# In[2]:


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.meetup.com/find/events/?allMeetups=true&radius=25&userFreeform=New York, NY&mcId=c10001&mcName=New York, NY'

response=requests.get(url,headers=headers)


soup=BeautifulSoup(response.content,'lxml')


# In[ ]:




