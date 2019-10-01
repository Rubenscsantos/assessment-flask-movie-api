from os import getenv
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_swagger_ui import get_swaggerui_blueprint
import requests
import json

app = Flask(__name__)
api = Api(app)


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Assessment Movie API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

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

class HealthCheck(Resource):
    def get(self):
        return "Health check"

api.add_resource(HealthCheck, '/')
api.add_resource(MovieGenres, '/api/v1/filmes/generos')

if __name__ == '__main__':
    port = int(getenv('PORT', 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
