from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

def connect():
    #Create a engine for connecting to SQLite3.
    e = create_engine('sqlite:///salaries.db', echo=True)

        