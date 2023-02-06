#!/usr/bin/env python3
""" Auth Class."""
from flask import request
import re
from typing import List, TypeVar


class Auth:
    """ Manage the API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Implements the API authentication mgt."""
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Implements autherization header."""
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Implements the current user request status."""
        return None
