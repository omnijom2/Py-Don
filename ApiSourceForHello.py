#!/usr/bin/env python
#This program is very basic
import pymongo
from pymongo import MongoClient
import json
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from bson.json_util import dumps
import datetime
client = MongoClient('127.0.0.1',27017)

db = client.pythonTest
db_inputs_col = db['input_entries']

app = Flask(__name__)
api = Api(app)
print("Hello World!")

class inputEntry ():
    def __init__(self, inputVal):
        self.inputString = inputVal
    def inputEntryObj(self):
        return {"inputValue": self.inputString, "asked_date": str(datetime.datetime.now())}

def cmd_line_input ():
    incomingMessage = input("\n\nEnter File Path fpr Reading please\n\n")
    return incomingMessage

def fullFileString (path):
    fileForReading = open(path,'r')
    return fileForReading.read()
    
def new_printer (incoming_string):
    string_for_using = incoming_string
    entryObj = inputEntry(string_for_using)
    print('Printing: '+ entryObj.inputString)
    response = db_inputs_col.insert(entryObj.inputEntryObj())
    return response

@app.route('/sendMessage', methods=['POST'])
def add_message():
    message = (request.get_json())
    objectId = new_printer(message['message'])
    return str(objectId), 200

@app.route('/getMessages', methods=['GET'])
def get_messages():
    docs = db_inputs_col.find()
    docs = dumps(docs)
    return docs, 200

app.run()
# new_printer(cmd_line_input, fullFileString)
#lambda cmd_line_input, new_printer  : new_printer(cmd_line_input)

        