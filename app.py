from flask import Flask
from flask import request
from flask_restx import Api, Resource, fields, reqparse
from db import Database

flask_app = Flask(__name__)
app = Api(app = flask_app)

namespace = app.namespace('pokemon', description='Pokemon APIs')
sort_parser = reqparse.RequestParser()
sort_parser.add_argument("order", type=str)
sort_parser.add_argument("column", type=str)
sort_parser.add_argument("limit", type=int)

filter_parser = reqparse.RequestParser()
filter_parser.add_argument("type", type=str)

db = Database()

@namespace.route("/")
class PokemonApi(Resource):
    def get(self):
        return {
            "pokemon": db.returnAll()
        }

@namespace.route("/sortBy")
class PokemonApi(Resource):

    @namespace.expect(sort_parser)
    def get(self):
        args = sort_parser.parse_args()
        return {
            "pokemon": db.sortBy(args['column'], args['order'], args['limit'])
        }

@namespace.route("/filterBy")
class PokemonApi(Resource):

    @namespace.expect(filter_parser)
    def get(self):
        args = filter_parser.parse_args()
        return {
            "pokemon": db.filterBy(args['type'])
        }