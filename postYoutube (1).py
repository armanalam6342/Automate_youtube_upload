#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pendulum
print(f"Execution started at {pendulum.now().to_datetime_string()}")
import youtube_upload
import argparse
import pandas as pd
import sys
sys.path.insert(1, '/home/ubuntu/')




import os
import random


df  = pd.read_csv("youtube/islamicShorts.csv")




file_path = df["path"][0]


# In[5]:


des = """Welcome to Islamic Insights, your source for enriching Islamic wisdom. 
In this video, we bring you a collection of inspirational Islamic quotes that will illuminate your heart and mind. 
From the timeless words of the Prophet Muhammad (peace be upon him) to the profound verses of the Quran, 
these quotes offer guidance, comfort, and motivation for all aspects of life. 
Join us on this spiritual journey as we delve into the depths of Islamic wisdom and reflect on the beauty of 
faith, resilience, and gratitude. 
Whether you seek solace in times of hardship or inspiration for daily living, 
these quotes are a beacon of light for every soul. 
Subscribe to Islamic Insights for more enlightening content and let the light of Islam illuminate your path. 
#IslamicQuotes #Inspiration #Faith #Resilience #Gratitude #IslamicWisdom #Spirituality #IslamicInsights"""


# In[6]:


title = "#IslamicVideo #IslamicWisdom #MuslimQuotes #QuranicWisdom"
tags= "Islamic Teachings,Quranic Wisdom,Islamic Culture,Quran Explanation,Hadith Studies,Islamic Lifestyle,Muslim Faith,Islamic Scholars,Spiritual Growth Islam,Islamic Education,Contemporary Muslim Issues,Islamic Traditions,Islamic Heritage,Islamic Art and Architecture,Islamic Ethics,Interfaith Dialogue Islam,Islamic Science Contributions,islamic video,hadees,islamic history,islamic insignts,hindi islamic video,islamic video hindi"


# In[7]:


import subprocess

def run_upload_video(file,title,key):
    # Command to execute
    global des
    command = [
        "python3",
        "youtube/youtube_upload.py",
        f"--file={file}",
        f"--title={title}",
        f"--description={des}",
        f"--keywords={key}",
        "--category=22",
        "--privacyStatus=public"
    ]
    
    # Execute the command
    subprocess.run(command)




run_upload_video(file_path,title,tags)




df[1:].to_csv("youtube/islamicShorts.csv",index= False)


import pendulum
print(f"Execution started at {pendulum.now().to_datetime_string()}")
# In[ ]:




