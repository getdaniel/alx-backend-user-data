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
            for ex_paths in map(lambda x: x.strip(), excluded_paths):
                pattern = ''

                if ex_paths[-1] == '*':
                    pattern = '{}.*'.format(ex_paths[0:-1])
                elif ex_paths[-1] == '/':
                    pattern = '{}./*'.format(ex_paths[0:-1])
                else:
                    pattern = '{}./*'.format(ex_paths)

                if re.match(pattern, path):
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
