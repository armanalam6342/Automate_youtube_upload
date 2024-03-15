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


df  = pd.read_csv("youtube.csv")




file_path = df["path"][0]


# In[5]:


des = description


# In[6]:


title = title
tags= tags


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




df[1:].to_csv("youtube.csv",index= False)


import pendulum
print(f"Execution started at {pendulum.now().to_datetime_string()}")
# In[ ]:




