'''
Adapted from "Build and deploy a Flask CRUD API with Firestore and Cloud Run"
Author: @timtech4u
https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run
'''

# Required imports
import os
from flask import Flask, request, render_template
#from firebase_admin import credentials, firestore, initialize_app


# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
#cred = credentials.Certificate('key.json')
#default_app = initialize_app(cred)
#db = firestore.client()
#todo_ref = db.collection('todos')
'''
from google.cloud import firestore
try:
    import google.auth
    from google.cloud import secretmanager_v1beta1 as sm
except ImportError:
    print("Import Error raised.")
    pass

def my_reddit_comments():
    db = firestore.Client()
    coll = db.collection('tagapagtuos_submissions').stream()
    db = None
    return [doc.to_dict() for doc in coll]

@app.route('/sample', methods=['GET'])
def sample():
    context = my_reddit_comments()
    return render_template('sample.html', context=context)
'''
@app.route('/')
def home():
    return render_template('home.html')

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)