#!/usr/bin/env python3
""" Authentication class."""
from typing import List, TypeVar
from flask import request
import os


class Auth:
    """ Implements Authentication of users."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Execute for authentication before any request.
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for ex_path in excluded_paths:
            if path == ex_path or path.startswith(ex_path[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Autherization header message retriver
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ The current user status
        """
        return None

    def session_cookie(self, request=None):
        """ Implements session cookies."""
        if request is None:
            return None

        session_name = os.environ.get("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_name)
