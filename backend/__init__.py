import os

from flask import Flask, jsonify
from flask_cors import CORS
from . import db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        db.init_db()

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/test', methods=['GET'])
    def test():
        output = {
            'id': "boi",
            'title': "test"
        }
        

        db.insert_location("sydney", "earth", 5)

        results = db.query_db("SELECT * FROM LOCATION")
        for a in results:
            print(a["city_name"])
        return jsonify(output)

    return app