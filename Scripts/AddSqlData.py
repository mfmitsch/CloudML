#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:29:46 2023

@author: michaelmitschjr
"""
import pymysql
from flask import Flask, render_template, request,jsonify

def MakeMySqlConnection():
   while(True):
      try:
         username = input("MySQL database master username: ")
         password = input("MySQL database password: ")
         host = input("MySQL host url: ")
         db = pymysql.connect(host=host, user=username, password=password)
         break
      except:
         print("\nIncorrect Credentials\n")
   return db
         


def CreateNewDataTable(db):
   pass

def AddToExistingDataTable(datasetName, googleSheetID, keyColumn):
   msg = {"name": datasetName,
          "id": googleSheetID,
          "key": keyColumn}
   return jsonify(msg)

def AddTrainedModel(db):
   pass
