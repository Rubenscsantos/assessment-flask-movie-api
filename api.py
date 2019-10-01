from os import getenv
from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
import json

app = Flask(__name__)
api = Api(app)

class MovieGenres(Resource):
    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument("user_id", type=str)

        args = parser.parse_args()

        auth = requests.get("https://assessment-node-api.herokuapp.com/api/v1/users/{args}".format(args=args.user_id)).text
        if(auth != "null"):
            key = getenv("MOVIE_DATABASE_API_KEY", "")
            response = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key={key}&language=pt-BR".format(key=key)).text
            return json.loads(response)
        else:
            return "user_id is invalid"


api.add_resource(MovieGenres, '/filmes/generos')

if __name__ == '__main__':
    app.run(debug=True)