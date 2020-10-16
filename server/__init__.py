import os

from flask import Flask, jsonify, request, make_response, render_template
from flask_cors import CORS
from . import spaceship as ss

BAD_REQUEST = "400 Bad Request"
NO_CONTENT = "204 No Content"

def is_int(string):
    try:
        
        int(string)
        print("IS INT")
        return True
    except ValueError:
        return False

def make_status_response(status):
    response = make_response()
    response.status = status
    
    return response





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
    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')

    @app.route('/test', methods=['GET', 'POST'])
    def test():
        loc = ss.insert_location("sydney", "earth", 1)
        loc2 = ss.insert_location("melbourne", "earth", 0)

        new_ship = ss.insert_ship("bob", "john", "broken", loc2)


        if (ss.get_location_by_id(loc)):
            print("LOCATION STILL THERE")
        else:
            print("LOCATION DELETED")
        
        output = ss.get_ship_by_id(new_ship)

        return jsonify(output)

    # Returns a JSON payload of a ship given a ship ID
    @app.route('/ships/<id>', methods=['GET'])
    def ships_id(id):
        if not is_int(id):
            return make_status_response(BAD_REQUEST)

        ship = ss.get_ship_by_id(id)
        
        if ship:
            return jsonify(ship)
        else:
            return make_status_response(NO_CONTENT)

        return response


    @app.route('/ships', methods=['POST'])
    def ships_insert():
        payload = request.get_json()
        print(payload)
        # Checks validity of call
        if not payload:
            print("AERE")
            return make_status_response(BAD_REQUEST)

        print("PAYLOAD EXISTS")
        valid_input = True
        attr_list = ["name", "model", "status", "location_id"]

        if not all(attr in payload for attr in attr_list):
            print("HERE")
            return make_status_response(BAD_REQUEST)

        # Adds ship to db
        new_id = ss.insert_ship(payload["name"], payload["model"], payload["status"], payload["location_id"])
        
        if (new_id):
            print("SUCCESS")
            return jsonify({ 'id': new_id })
        else:
            print("BERE")
            return make_status_response(BAD_REQUEST)

    # Returns a JSON payload of a ship given a ship ID
    @app.route('/locations/<id>', methods=['GET'])
    def locations_id(id):
        if not is_int(id):
            return make_status_response(BAD_REQUEST)

        location = ss.get_location_by_id(id)
        
        if location:
            return jsonify(location)
        else:
            return make_status_response(NO_CONTENT)

        return response

    @app.route('/locations', methods=['POST'])
    def locations_insert():
        payload = request.get_json()
        print(payload)
        # Checks validity of call
        if not payload:
            print("AERE")
            return make_status_response(BAD_REQUEST)

        print("PAYLOAD EXISTS")
        valid_input = True
        attr_list = ["city", "planet", "capacity"]

        if not all(attr in payload for attr in attr_list):
            print("HERE")
            return make_status_response(BAD_REQUEST)

        # Adds ship to db
        new_id = ss.insert_location(payload["city"], payload["planet"], payload["capacity"])
        
        if (new_id):
            ss.print_row(ss.get_location_by_id(new_id))
            return jsonify({ 'id': new_id })
        else:
            print("BERE")
            return make_status_response(BAD_REQUEST)

    return app

    