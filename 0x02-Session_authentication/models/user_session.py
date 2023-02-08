#!/usr/bin/env python3
""" Session in Database."""
from models.base import Base


class UserSession(Base):
    """ Implements the user session class."""

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize user session class."""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
