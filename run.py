"""Flask App Entry."""
from flask import Flask
from flask.json import jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from apps.DogBreedDetector import DogBreedDetector
from apps.download_models import download_dog_breed_model

UPLOAD_FOLDER = 'static/uploads'

#  Create a Flask WSGI application
app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['JSON_SORT_KEYS'] = False
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": ["*"]}})


class Home(Resource):
    """Root Route."""

    def get(self):
        """Send The Api list."""
        return jsonify({
            'name': 'Abhyasa App',
            'apis': {
                'POST /dog-breed-detector': 'Accepts a file - dog pic, returns a json with dog\'s breed name'
            }
        })


api.add_resource(Home, '/')
api.add_resource(DogBreedDetector, '/dog-breed-detector')

download_dog_breed_model()

if __name__ == "__main__":
    app.run()
