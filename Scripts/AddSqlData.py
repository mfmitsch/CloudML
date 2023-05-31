#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:29:46 2023

@author: michaelmitschjr
"""
import pymysql
from flask import Flask, render_template, request,jsonify
import LoadGoogleData
import pickle
import getpass

ADD_DATA_INSTANCE_SQL = '''
insert into dataInstances(datasetId,
                          featureValues,
                          keyValue)
values('%s','%s','%s')
'''
ADD_MODEL_INSTANCE_SQL = '''
insert into models(datasetId,
                          model)
values('%s','%s')
'''
ADD_DATASET_SQL = '''
insert into datasets(datasetId,
                          featureNames,
                          dataName,
                          targetName)
values('%s','%s','%s','%s')
'''
db = None

def MakeMySqlConnection():
   while(True):
      try:
         username = input("MySQL database master username: ")
         password = getpass.getpass()
         host = input("MySQL host url: ")
         global db
         db = pymysql.connect(host=host, user=username, password=password, database="TrainingData")
         break
      except:
         print("\nIncorrect Credentials\n")
         if(input("Try again?") != 'N'):
            continue
      return
   
def GetDatasets():
   sql = '''select dataName from datasets'''        
   

def CreateTrainingDataTable(db):
   sql = '''create table dataInstances ( instanceId int not null auto_increment, datasetId varchar(100), featureValues BLOB, 
   keyValue float, primary key (instanceId), foreign key (datasetId) references datasets(datasetId))'''
   cursor = db.cursor()
   cursor.execute(sql)

def CreateModelTable(db):
   sql = '''create table models ( modelId int not null auto_increment, datasetId varchar(100), 
   model BLOB, primary key (modelId), foreign key (datasetId) references datasets(datasetId))'''
   cursor = db.cursor()
   cursor.execute(sql)

def CreateDataSetTable(db):
   sql = '''create table datasets ( datasetId varchar(100), featureNames BLOB, dataName varchar(50), 
   targetName varchar(50), primary key (datasetId))'''
   cursor = db.cursor()
   cursor.execute(sql)

#url = 'https://drive.google.com/uc?export=download&id=1DHGZ82GJJA4kLwRqjurEv419tnkcjaNW'
def AddToExistingDataTable(datasetName, googleSheetID, keyColumn):
   df = LoadGoogleData.google_data_Server(googleSheetID)
   targetValues = df[keyColumn]
   featureDataFrame = df.drop(columns = [keyColumn])
   featureNames = featureDataFrame.columns
   featureValues = featureDataFrame.values
   pickledFeatureNames = str(pickle.dumps(featureNames,0))[2:-1]
   #pickledFeatureNames = pickle.dumps(featureNames).decode()
   cursor = db.cursor()
   sql = ADD_DATASET_SQL % (googleSheetID,pickledFeatureNames,datasetName,keyColumn)
   cursor.execute(sql)
   
   for instance, target in zip(featureValues,targetValues):
      pickledFeatureValue = str(pickle.dumps(instance,0))[2:-1]
      #pickledFeatureValue = pickle.dumps(instance).decode()
      sql = ADD_DATA_INSTANCE_SQL % (googleSheetID,pickledFeatureValue,str(target))
      try:
         cursor.execute(sql)
      except:
         print("data skipped")
         #print(instance)
   
   db.commit()
   
   msg = {"name": datasetName,
          "id": googleSheetID,
          "key": keyColumn}
   return jsonify(msg)

def AddTrainedModel(model, dataSetId):
   cursor = db.cursor()
   sql = ADD_MODEL_INSTANCE_SQL % (dataSetId, model.decode())
   cursor.execute(sql)
   db.commit()
