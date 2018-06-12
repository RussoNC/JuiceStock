from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

class sqlProcess:
    def __init__(self):
        self.addrs = ""
        