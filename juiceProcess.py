from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine, MetaData, Table
from json import dumps
from datetime import datetime, date

#Create a engine for connecting to SQLite3.
e = create_engine('sqlite:///juiceStock.db', echo=True)

#Retreives and send list of all items on the table
def getJuices():
    conn = e.connect()
    query = conn.execute("select * from juice")
    #Query the result and get cursor.Dumping that data to a JSON is looked by extension
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    conn.close()
    return result

#Retrieves and send all data of matching id 
def getJuice(id):
    conn = e.connect()
    query = conn.execute("select * from juice where id ="+id)
    #Query the result and get cursor.Dumping that data to a JSON is looked by extension
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    conn.close()
    return result
    
#Adds one record to the table
def juiceAdd(idArg,date_fabricatedArg,descArg,quantityArg,nic_valueArg,date_steepedArg):
    #Lets format dates so sql3 accepts it :
    datetime_fabricatedArg = datetime.strptime(date_fabricatedArg, '%Y-%m-%d %H:%M:%S')
    datetime_steepedArg    = datetime.strptime(date_steepedArg,    '%Y-%m-%d %H:%M:%S')
    conn = e.connect()
    # Create MetaData instance
    metadata = MetaData(e, reflect=True) #TODO remove this (only for dev)
    # Get Table
    juicesTable = metadata.tables['juice']
    ins = juicesTable.insert().values(id=idArg,date_fabricated=datetime_fabricatedArg,desc=descArg,quantity=quantityArg,nic_value=nic_valueArg,date_steeped=datetime_steepedArg)      
    result = conn.execute(ins)
