from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app.doc = '/docs')
