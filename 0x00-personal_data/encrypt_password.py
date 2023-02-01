#!/usr/bin/env python3
""" Encrypting Password."""
from bcrypt import checkpw, gensalt, hashpw


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string."""
    return hashpw(password.encode('utf-8'), gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks valid password."""
    return checkpw(password.encode('utf-8'), hashed_password)
