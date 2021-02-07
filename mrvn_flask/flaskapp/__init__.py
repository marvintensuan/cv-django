import os
import environ
from flask import Flask

try:
    import google.auth
    from google.cloud import secretmanager_v1beta1 as sm
except ImportError:
    print("Import Error raised.")
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file = os.path.join(BASE_DIR,  ".env")

SETTINGS_NAME = "flask_app_settings"

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if not os.path.isfile('.env'):
        _, project = google.auth.default()

    if project:
        client = sm.SecretManagerServiceClient()
        path = client.secret_version_path(project, SETTINGS_NAME, "latest")
        payload = client.access_secret_version(path).payload.data.decode("UTF-8")

        with open(env_file, "w") as f:
            f.write(payload)

    app.config.from_mapping(
        env = environ.Env()
        env.read_env(env_file)
        SECRET_KEY= env('SECRET_KEY'),
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "env('GOOGLE_APPLICATION_CREDENTIALS')"
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import home
    app.register_blueprint(home.bp)

    return app