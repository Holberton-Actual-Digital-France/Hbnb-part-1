from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
jwt = JWTManager(app)

# Authenticated endpoint: Submit Reviews
@app.route('/places/<int:place_id>/reviews', methods=['POST'])
@jwt_required()
def submit_review(place_id):
    current_user = get_jwt_identity()
    # Logic to submit a review for place_id by current_user
    return jsonify({"message": "Review submitted successfully"}), 200

# Authenticated endpoint: Edit Reviews (for reviews created by the user)
@app.route('/places/<int:place_id>/reviews', methods=['PUT'])
@jwt_required()
def edit_review(place_id):
    current_user = get_jwt_identity()
    # Logic to edit the review for place_id by current_user
    return jsonify({"message": "Review edited successfully"}), 200

# Authenticated endpoint: Manage Places (Create, Update, Delete - owned by the user)
@app.route('/places', methods=['POST'])
@jwt_required()
def create_place():
    current_user = get_jwt_identity()
    # Logic to create a new place owned by current_user
    return jsonify({"message": "Place created successfully"}), 200

@app.route('/places/<int:place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    current_user = get_jwt_identity()
    # Logic to update place details for place_id owned by current_user
    return jsonify({"message": "Place updated successfully"}), 200

@app.route('/places/<int:place_id>', methods=['DELETE'])
@jwt_required()
def delete_place(place_id):
    current_user = get_jwt_identity()
    # Logic to delete place for place_id owned by current_user
    return jsonify({"message": "Place deleted successfully"}), 200
