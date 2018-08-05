#!/usr/bin/env python
#This program is very basic
import pymongo
from pymongo import MongoClient
import json
import datetime
client = MongoClient('127.0.0.1',27017)

db = client.pythonTest
db_inputs_col = db['input_entries']

print("Hello World!")


class inputEntry ():
    def __init__(self, inputVal):
        self.inputString = inputVal
    def inputEntryObj(self):
        return {"inputValue": self.inputString, "asked_date": str(datetime.datetime.now())}

def cmd_line_input ():
    incomingMessage = input("\n\nWhat would you like me to Print?\n\n")
    return incomingMessage

def new_printer (incoming_string):
    entryObj = inputEntry(incoming_string())
    print('Printing: '+ entryObj.inputString)
    db_inputs_col.insert_one(entryObj.inputEntryObj())
    return incoming_string


new_printer(cmd_line_input)
#lambda cmd_line_input, new_printer  : new_printer(cmd_line_input)

        