from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
jwt = JWTManager(app)

# Protected Admin endpoint: Manage Amenities (Admin only)
@app.route('/amenities', methods=['POST'])
@jwt_required()
def create_amenity():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"message": "Admin privileges required"}), 403

    # Logic to create a new amenity
    return jsonify({"message": "Amenity created successfully"}), 200

@app.route('/amenities/<int:amenity_id>', methods=['DELETE'])
@jwt_required()
def delete_amenity(amenity_id):
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"message": "Admin privileges required"}), 403

    # Logic to delete an amenity by amenity_id
    return jsonify({"message": "Amenity deleted successfully"}), 200

# Similar protected admin endpoints for managing cities, users, and places
# Example routes: POST /cities, DELETE /cities/<city_id>
# Example routes: POST /users, PUT /users/<user_id>, DELETE /users/<user_id>
# Example routes: POST /places, PUT /places/<place_id>, DELETE /places/<place_id>
