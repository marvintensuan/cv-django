'''
Adapted from "Build and deploy a Flask CRUD API with Firestore and Cloud Run"
Author: @timtech4u
https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run
'''

import os
from flask import Flask, render_template
from dotenv import load_dotenv

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

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list_of_cpds')
def learning_cpd():
    return render_template('list_of_cpds.html')

@app.route('/self_directed_learning')
def learning_sdl():
    return render_template('self_directed_learning.html')

@app.route('/my_learning_roadmap')
def learning_roadmap():
    return render_template('my_learning_roadmap.html')

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)