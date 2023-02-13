#!/usr/bin/env python3
""" Basic Flask App."""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
