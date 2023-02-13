#!/usr/bin/env python3
""" Authentication Implementation modules."""
import bcrypt
from db import DB
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

def _generate_uuid() -> str:
    """ Generates UUIDs."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initialize the auth."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The newly created User object.

        Raises:
            ValueError: If a user already exists with the passed email.
        """
        try:
            self._db.find_user_by(email=email)
        except:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Try locating the user by email.
        If it exists, check the password with bcrypt.checkpw.
        If it matches return True. In any other case, return False.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ Create user session."""
        try:
            user = self._db.find_user_by(email=email)
        except:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id
