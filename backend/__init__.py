import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from . import spaceship as ss

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

    @app.route('/test', methods=['GET', 'POST'])
    def test():
        output = {
            'id': "boi",
            'title': "test"
        }

        loc = ss.insert_location("sydney", "earth", 1)
        loc2 = ss.insert_location("melbourne", "earth", 0)

        new_ship = ss.insert_ship("bob", "john", "broken", loc)

        ss.delete_location(loc)

        if (ss.get_location_by_id(loc)):
            print("LOCATION STILL THERE")
        else:
            print("LOCATION DELETED")

        ss.print_row(ss.get_ship_by_id(new_ship))

        return jsonify(output)

    return app