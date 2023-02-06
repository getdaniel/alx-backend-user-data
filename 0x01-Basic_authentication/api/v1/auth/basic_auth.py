#!/usr/bin/env python3
""" Basic Auth."""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Defines basic authentication."""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Implements base64 part of Base."""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        
        if not authorization_header.startswith("Basic "):
            return None
        
        return authorization_header.split("Basic ")[1]
