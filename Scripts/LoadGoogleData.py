#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:30:40 2020
@author: michaelmitschjr
Imports data from csv in google that is viewable by anyone
"""
import requests
import pandas as pd

def google_data_Server(id):
   url = "https://docs.google.com/spreadsheets/d/"+ id +"/export?format=csv&gid=0"
   #url = 'https://drive.google.com/uc?export=download&id=' + id
   r = requests.get(url, allow_redirects=True)
   string_csv = r.content.decode('utf-8').split('\n')
   features = string_csv[0].strip().split(",")[1:]   
   data = [eval('['+line+']')[1:] for line in string_csv[1:len(string_csv)-1]]
   df = pd.DataFrame(data, columns = features) 
   return df