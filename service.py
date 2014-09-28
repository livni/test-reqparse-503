from flask import Flask
from flask.ext.restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Test1(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('something', type=str, required=True, location='json')

    def post(self):
        self.parser.parse_args()
        return 'ok'
api.add_resource(Test1, '/test1')

class Test2(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # self.parser.add_argument('something', type=str, required=True, location='json')

    def post(self):
        self.parser.parse_args()
        return 'ok'
api.add_resource(Test2, '/test2')

class Test3(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('something', type=str, required=True, location='json')

    def post(self):
        # self.parser.parse_args()
        return 'ok'
api.add_resource(Test3, '/test3')

class Test4(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # self.parser.add_argument('something', type=str, required=True, location='json')

    def post(self):
        # self.parser.parse_args()
        return 'ok'
api.add_resource(Test4, '/test4')
