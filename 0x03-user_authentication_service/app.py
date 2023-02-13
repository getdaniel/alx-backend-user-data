#!/usr/bin/env python3
""" Basic Flask App."""
from flask import abort, Flask, jsonify, redirect, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ Routes with GET /."""
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """ Register new user by POST /users."""
    try:
        email = request.form['email']
        password = request.form['password']
        user = AUTH.register_user(email, password)
        return jsonify({'email': user.email, 'message': 'user created'})
    except ValueError:
        return jsonify({'message': "email already registered"}), 400

@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Login session."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response

@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Log out the user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
