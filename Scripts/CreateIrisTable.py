#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:53:34 2023

@author: michaelmitschjr
"""

#cloudml.cxpkh4e28v4d.us-east-2.rds.amazonaws.com
import pymysql
host = "cloudml.cxpkh4e28v4d.us-east-2.rds.amazonaws.com"
user = "mfmitsch"
password = "$123Luke"

db = pymysql.connect(host=host, user=user, password=password)

