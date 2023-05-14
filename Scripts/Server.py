#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:16:02 2023

@author: michaelmitschjr
"""
import connexion
from flask import Flask, render_template, request,jsonify
import AddSqlData

def test(i):
   msg = {"msg": i}
   return jsonify(msg)

app = connexion.App(__name__, specification_dir="./")

app.add_api("master.yaml")

#DataBaseConnection = AddSqlData.MakeMySqlConnection()

@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(port=8080, debug=False)