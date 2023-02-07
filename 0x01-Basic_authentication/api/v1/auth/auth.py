#!/usr/bin/env python3
""" Authentication class."""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Implements Authentication of users."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Execute for authentication before any request.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/.*'.format(exclusion_path)

                if re.match(pattern, path):
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
