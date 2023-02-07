#!/usr/bin/env python3
""" Basic authentication class."""
from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """ Defines basic authentication."""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """ Implements base64 part of Base."""
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """ Decodes the base64 autherization header."""
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(
                    base64_authorization_header).decode('utf-8')
        except (UnicodeDecodeError, binascii.Error):
            return None

        return decoded
