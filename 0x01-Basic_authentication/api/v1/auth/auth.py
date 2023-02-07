#!/usr/bin/env python3
""" Authentication class."""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Implements Authentication of users."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False
        """
        if not path:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        for p in excluded_paths:
            if path == p[:-1] or path.startswith(p):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns None
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None
        """
        return None
