from flask_restful import Resource
from flask import flash, request, url_for, jsonify


class DogBreedDetector(Resource):
    def allowed_file(filename):
        """Check whether the given filename is allowed."""
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def get(self): return {'name': 'DogBreedDetector'}

    def post(self):
        """Dog breed detector."""
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return jsonify({
                'success': False,
                'message': 'File not found in request payload'
            })

        file = request.files['file']
        # if user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return jsonify({
                'success': False,
                'message': 'File not found in request payload'
            })

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({
                'success': True,
                'fileurl': url_for('uploaded_file',
                                   filename=filename)
            })
