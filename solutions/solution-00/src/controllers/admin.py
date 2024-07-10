from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt

# protected endpoint that requires admin role
@app.route('/admin/data', methods=['POST', 'DELETE'])
@jwt_required()
def admin_data():
    claims = get_jwt()

    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

    # Proceed with admin-only functionality
    return jsonify({"msg": "Admin action successful"}), 200
