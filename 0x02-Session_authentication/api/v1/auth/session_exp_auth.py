#!/usr/bin/env python3
""" Expiration Session"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """ Implements expiration class."""
    def __init__(self):
        """ Initialize SessionExpAuth class."""
        super().__init__()
        self.session_duration = int(os.environ.get('SESSION_DURATION', 0))

    def create_session(self, user_id=None):
        """ Creates a session."""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Creates session id for user id."""
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dict['user_id']

        if 'created_at' not in session_dict:
            return None

        created_at = session_dict['created_at']
        date_time = created_at + timedelta(seconds=self.session_duration)
        if date_time < datetime.now():
            return None

        return session_dict['user_id']
