#!/usr/bin/env python3
""" Session Authentication."""
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
import os
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """POST /api/v1/auth_session/login
    Return:
      - JSON representation of a User object.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})

    if len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response


@app_views.route(
        '/auth_session/logout', methods=['DELETE'], strict_slashes=True)
def logout():
    """ Destroy the session when logout."""
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)

    response = jsonify({})
    response.delete_cookie(os.getenv('SESSION_NAME'))

    return response, 200
