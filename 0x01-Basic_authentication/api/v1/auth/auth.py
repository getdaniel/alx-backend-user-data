#!/usr/bin/env python3
""" Authentication class."""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Implements Authentication of users."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None
        """
        return None
