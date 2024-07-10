from flask import Flask, jsonify

app = Flask(__name__)

# Public endpoint: User Login
@app.route('/login', methods=['POST'])
def login():
    # Authentication logic would go here
    # For demonstration, just return a success message
    return jsonify({"message": "User logged in successfully"}), 200

# Public endpoint: View Places
@app.route('/places', methods=['GET'])
def get_places():
    # Logic to fetch places from database
    places = [{'id': 1, 'name': 'Place A'}, {'id': 2, 'name': 'Place B'}]
    return jsonify(places), 200

# Public endpoint: View Place Details
@app.route('/places/<int:place_id>', methods=['GET'])
def get_place_details(place_id):
    # Logic to fetch place details by place_id
    place = {'id': place_id, 'name': f'Place {place_id}', 'description': 'Details of the place'}
    return jsonify(place), 200
