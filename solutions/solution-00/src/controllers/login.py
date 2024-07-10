from flask import jsonify, request
from flask_jwt_extended import create_access_token
from models import User  # Assuming User model is defined in models module

def login():
    # Authenticate user (example)
    user = User.query.filter_by(email=request.json['email']).first()

    if not user or not user.check_password(request.json['password']):
        return jsonify({"msg": "Invalid credentials"}), 401

    # Create JWT with additional claims (is_admin)
    additional_claims = {"is_admin": user.is_admin}
    access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)

    return jsonify(access_token=access_token)
