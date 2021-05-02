import os
import urllib.request
from flask import Flask,request,redirect,jsonify
from werkzeug.utils import secure_filename
from __init__ import app
from models import view

ALLOWED_EXTENSIONS = set(['txt', 'pdf','docx'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        resp=jsonify({'Message':'No file part in the request'})
        resp.status_code=400
        return resp

    files=request.files.getlist('files')

    errors={}
    success=False
    file_names=[]
    for file in files:
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            # db_resp=db.insert(filename)
            file_names.append(filename)
            success=True

        else:
            errors[file.filename]='File not found'

    # if(success and errors):
    #     errors['message']='File(s) uploaded successfully !'
    #     resp=jsonify(errors)
    #     resp.status_code=500
    #     return resp

    if(success):
        db_resp=view(file_names)
        resp=jsonify({'message':'Files uploaded successfully ! '+str(db_resp)})
        resp.status_code=201
        return resp

    else:
        resp=jsonify(errors)
        resp.status_code=500
        return resp

if __name__=='__main__':
    app.run(debug=True)