"""Dog Breed Detector."""
import os
from flask_restful import Resource
from flask import flash, request, jsonify
from werkzeug.utils import secure_filename
from fastai.learner import load_learner
from fastai.vision.core import PILImage

import coloredlogs
import logging

# Create a logger object.
logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.DEBUG)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'static/uploads'
model_path = os.path.abspath('downloaded-models/dog_learner.pkl')


class DogBreedDetector(Resource):
    """Dog Breed Detector."""

    def allowed_file(self, filename):
        """Check whether the given filename is allowed."""
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def get_dog_details(self, img):
        """Use pre trained model and get dog details."""
        if os.path.exists(model_path):
            logger.info("Invoking Model:" + model_path)
            learn_inference = load_learner(model_path)
            logger.info("Running Predictor...")
            img = PILImage.create(img)
            pred, pred_idx, probs = learn_inference.predict(img)
            logger.info('Predicted Result:' + str(pred))
            return {
                'success': True,
                'pred': str(pred),
                # 'pred_idx': pred_idx,
                # 'probs': probs
            }
        else:
            logger.debug("Model not found:" + model_path)
            return {
                'success': False,
                'message': 'Apologies. Model not found'
            }

    def get(self):
        """Get the details of this api."""
        return {
            'name': 'DogBreedDetector',
            'message': 'You need to use POST:dog-breed-detector to upload' +
            ' a pic of a dog.'
        }

    def post(self):
        """Dog breed detector."""
        # check if the post request has the file part
        logger.info("------Dog breed detector------")
        logger.info('request.files = ' + str(request.files))
        if 'File' not in request.files:
            flash('No file part')
            return jsonify({
                'success': False,
                'message': 'File not found in request payload \'file\' not' +
                ' in request.files'
            })

        file = request.files['File']
        logger.info('file', str(file))
        # if user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return jsonify({
                'success': False,
                'message': 'File not found in request payload'
            })

        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            result = self.get_dog_details(file)
            pred = result['pred']
            if(pred == 'dobar man'):
                pred = 'Doberman'
            elif(pred == 'dolmation'):
                pred = 'Dalmatian'

            if result['success']:
                return jsonify({
                    'success': True,
                    'breed': pred,
                    'message': 'Received file ' + filename
                })
            else:
                return jsonify(result)
            # To save the file
            # filename = secure_filename(file.filename)
            # target_location = os.path.join(UPLOAD_FOLDER, filename)
            # print('target_location', target_location)
            # file.save(os.path.join(UPLOAD_FOLDER, filename))
            # return jsonify({
            #     'success': True,
            #     'fileurl': url_for('uploaded_file',
            #                        filename=filename)
            # })

        return jsonify({
            {
                'success': False,
                'message': 'No file found in the request'
            }
        })
