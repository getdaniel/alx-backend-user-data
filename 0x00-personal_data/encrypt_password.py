#!/usr/bin/env python3
""" Encrypting Password."""
from bcrypt import gensalt, hashpw


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string."""
    return hashpw(password.encode('utf-8'), gensalt())
