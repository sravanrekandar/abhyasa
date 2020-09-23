"""Flask App Entry."""
import os
from flask import Flask, flash, request, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api
from .app.DogBreedDetector import DogBreedDetector
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

#  Create a Flask WSGI application
app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(DogBreedDetector, '/dog-breed-detector')


# @app.route("/")
# @app.route("/home/")
# def home():
#     """Home Page."""
#     title = "Sravan's Machine Learning Demos"
#     return f"""
#         <!Docstring html>
#         <html>
#             <header>
#                 <title>{title}</title>
#             </header>
#             <body>
#                 <h1>{title}</h1>
#                 <p>Home page content here.</p>
#             </body>
#         </html>
#     """


# @app.route('/dog-breed-detector', methods=['POST'])
# def dog_breed_detector():
#


# @app.errorhandler(404)
# def page_not_found(e):
#     """Not Found Page."""
#     title = "Flask Drive Page not found"
#     return f"""
#         <!Docstring html>
#         <html>
#             <header>
#                 <title>{title}</title>
#             </header>
#             <body>
#                 <h1>{title}</h1>
#                 <p>
#                     You seem to be lost!
#                     Please use navigation to go to right page
#                 </p>
#             </body>
#         </html>
#     """


if __name__ == "__main__":
    app.run()
