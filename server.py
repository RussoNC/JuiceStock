from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine, MetaData, Table
from json import dumps
from datetime import datetime
import logging
from datetime import date
import string

#Create a engine for connecting to SQLite3.
e = create_engine('sqlite:///salaries.db', echo=True)

app = Flask(__name__)
api = Api(app)

class Health(Resource):
    def get(self):
        return {'health': 'ok'}, 200

class JuiceInfoList(Resource):
    #def get(self, department_name):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from juice")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        conn.close()

        
class JuiceInfo(Resource):
    #def get(self, department_name):
    def get(self,juice_id):
        conn = e.connect()
        query = conn.execute("select * from juice where id ="+juice_id)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        conn.close()

class JuiceAdd(Resource):
    def post(self):
        #Get all params
        
        parser = reqparse.RequestParser()
        
        parser.add_argument('id', type=int, help='Numeric values only')
        parser.add_argument('date_fabricated', help='Date only')
        parser.add_argument('desc', help='String values only')
        parser.add_argument('quantity', type=int, help='Numeric values only')
        parser.add_argument('nic_value', type=int, help='Numeric values only')
        parser.add_argument('date_steeped', help='Numeric values only')
        args = parser.parse_args()
                
        idArg = args['id']
        date_fabricatedArg = args['date_fabricated']
        descArg = args['desc']
        quantityArg = args['quantity']
        nic_valueArg = args['nic_value']
        date_steepedArg = args['date_steeped']
        
        #Lets format dates so sql3 accepts it :
        datetime_fabricatedArg = datetime.strptime(date_fabricatedArg, '%Y-%m-%d %H:%M:%S')
        datetime_steepedArg    = datetime.strptime(date_steepedArg,    '%Y-%m-%d %H:%M:%S')
        
        conn = e.connect()
        
        # Create MetaData instance
        metadata = MetaData(e, reflect=True)
        # Get Table
        juicesTable = metadata.tables['juice']
        
        ins = juicesTable.insert().values(id=idArg,date_fabricated=datetime_fabricatedArg,desc=descArg,quantity=quantityArg,nic_value=nic_valueArg,date_steeped=datetime_steepedArg)
                
        result = conn.execute(ins)
        
        print(result)
        
        return 201
        
api.add_resource(JuiceInfoList, '/juices')
api.add_resource(JuiceAdd, '/juice/add')
api.add_resource(JuiceInfo, '/juice/<juice_id>')
api.add_resource(Health, '/health')

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=5002)
