'''
Adapted from "Build and deploy a Flask CRUD API with Firestore and Cloud Run"
Author: @timtech4u
https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run
'''

# Required imports
import os
from flask import Flask, request, render_template
#from firebase_admin import credentials, firestore, initialize_app
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
#cred = credentials.Certificate('key.json')
#default_app = initialize_app(cred)
#db = firestore.client()
#todo_ref = db.collection('todos')

try:
    from google.cloud import firestore
except:
    print('Cannot import google.cloud.firestore')

try:
    import google.auth
    from google.cloud import secretmanager as sm

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_file = os.path.join(BASE_DIR,  ".env")
    SETTINGS_NAME = "flask_app_settings"

    if not os.path.isfile('.env'):
        _, project = google.auth.default()

        if project:
            client = sm.SecretManagerServiceClient()
            path = client.secret_version_path(project, SETTINGS_NAME, "latest")
            payload = client.access_secret_version(path).payload.data.decode("UTF-8")

            with open(env_file, "w") as f:
                f.write(payload)
        
    load_dotenv()
except ImportError:
    print("Import Error raised.")

def my_reddit_comments():
    db = firestore.Client()
    coll = db.collection('tagapagtuos_submissions').stream()
    db = None
    return [doc.to_dict() for doc in coll]

@app.route('/sample', methods=['GET'])
def sample():
    context = my_reddit_comments()
    return render_template('sample.html', context=context)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list_of_cpds')
def learning_cpd():
    context = {'cpd_list': {}}
    return render_template('list_of_cpds.html', context=context)

@app.route('/self_directed_learning')
def learning_sdl():
    context = { 'webinar_list' : {},
                'onlinecourse_list': {}}
    return render_template('self_directed_learning.html', context=context)

@app.route('/my_learning_roadmap')
def learning_roadmap():
    return render_template('my_learning_roadmap.html')

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)