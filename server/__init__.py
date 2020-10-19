import os

from flask import Flask, jsonify, request, make_response, render_template
from flask_cors import CORS
from . import spaceship as ss

BAD_REQUEST = "400 Bad Request"
NO_CONTENT = "204 No Content"
SUCCESS = "200 OK"
# create and configure the app
app = Flask(__name__, instance_relative_config=True)
CORS(app)

def is_int(string):
    try:
        
        int(string)
        return True
    except ValueError:
        return False

def make_status_response(status):
    response = make_response()
    response.status = status
    
    return response

with app.app_context():
    db.init_db()

# a simple page that says hello
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

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
    # Checks validity of call
    if not payload:
        return make_status_response(BAD_REQUEST)

    valid_input = True
    attr_list = ["name", "model", "status", "location_id"]

    if not all(attr in payload for attr in attr_list):
        return make_status_response(BAD_REQUEST)

    # Adds ship to db
    new_id = ss.insert_ship(payload["name"], payload["model"], payload["status"], payload["location_id"])
    
    if (new_id):
        return jsonify({ 'id': new_id })
    else:
        return make_status_response(BAD_REQUEST)

@app.route('/ships/<id>', methods=['DELETE'])
def ships_del(id):
    if not is_int(id):
        return make_status_response(BAD_REQUEST)

    if not ss.delete_ship(id):
        return make_status_response(BAD_REQUEST)

    return jsonify({ 'deleted': "true" })



@app.route('/ships/status/<id>', methods=['POST'])
def status_update(id):
    payload = request.get_json()
    
    # Checks validity of call
    if not payload:
        return make_status_response(BAD_REQUEST)

    if "status" not in payload:
        return make_status_response(BAD_REQUEST)

    # Adds ship to db
    success = ss.change_ship_status(id, payload["status"])

    if (success):
        print("MADE IT")
        return jsonify({ 'status': payload["status"]} )
    else:
        return make_status_response(BAD_REQUEST)

@app.route('/ships/parking/<id>', methods=['POST'])
def ships_move(id):
    payload = request.get_json()
    
    # Checks validity of call
    if not payload:
        return make_status_response(BAD_REQUEST)

    if "location_id" not in payload:
        return make_status_response(BAD_REQUEST)

    # Adds ship to db
    success = ss.move_ship(id, payload["location_id"])

    if (success):
        return jsonify({ 'location_id': id })
    else:
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
    # Checks validity of call
    if not payload:
        return make_status_response(BAD_REQUEST)

    valid_input = True
    attr_list = ["city_name", "planet_name", "capacity"]

    if not all(attr in payload for attr in attr_list):
        return make_status_response(BAD_REQUEST)

    if not is_int(payload["capacity"]):
        return make_status_response(BAD_REQUEST)

    # Adds ship to db
    new_id = ss.insert_location(payload["city_name"], payload["planet_name"], payload["capacity"])
    
    if (new_id):
        ss.print_row(ss.get_location_by_id(new_id))
        return jsonify({ 'id': new_id })
    else:
        return make_status_response(BAD_REQUEST)


@app.route('/locations/<id>', methods=['DELETE'])
def locations_del(id):
    if not is_int(id):
        return make_status_response(BAD_REQUEST)

    if not ss.delete_location(id):
        return make_status_response(BAD_REQUEST)

    return jsonify({ 'deleted': "true" })
    
@app.route('/locations', methods=['GET'])
def locations_get_all():
    return jsonify(ss.get_locations())


@app.route('/locations/parked/<id>', methods=['GET'])
def locations_get_parked(id):
    return jsonify(ss.get_parked_ships(id))


