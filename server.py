from flask import Flask
from flask_restful import Resource, Api, reqparse

import juiceProcess

app = Flask(__name__)
api = Api(app)


class Health(Resource):
    def get(self):
        return {'health': 'ok'}, 200


class JuiceInfoList(Resource):
    def get(self):
        return juiceProcess.getJuices()
        

class JuiceInfo(Resource):
    def get(self,juice_id):
        return juiceProcess.getJuice(juice_id)


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
                
        id_arg = args['id']
        date_fabricated_arg = args['date_fabricated']
        desc_arg = args['desc']
        quantity_arg = args['quantity']
        nic_value_arg = args['nic_value']
        date_steeped_arg = args['date_steeped']
        
        juiceProcess.juiceAdd(id_arg, date_fabricated_arg, desc_arg, quantity_arg, nic_value_arg, date_steeped_arg)
        
        return 201
        
api.add_resource(JuiceInfoList, '/juices')
api.add_resource(JuiceAdd, '/juice/add')
api.add_resource(JuiceInfo, '/juice/<juice_id>')
api.add_resource(Health, '/health')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)
