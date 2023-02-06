#!/usr/bin/env python3
""" Auth Class."""
from flask import request
import re
from typing import List, TypeVar


class Auth:
    """ Manage the API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Implements the API authentication mgt."""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for ex_path in excluded_paths:
            if path == ex_path or path.startswith(ex_path[:-1]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Implements autherization header."""
        if request is not None:
            return request.headers.get('Authorization', None)

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Implements the current user request status."""
        return None
