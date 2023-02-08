#!/usr/bin/env python3
""" Database based session authentication."""
from datetime import datetime, timedelta
from flask import request
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ Implements session based on DB."""
    def create_session(self, user_id=None):
        """Creates and stores a session id for the user."""
        session_id = super().create_session(user_id)
        if type(session_id) == str:
            kwargs = {
                    'user_id': user_id,
                    'session_id': session_id,
                    }
            user_session = UserSession(**kwargs)
            user_session.save()
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieves the user id of the user associated with
        a given session id.
        """
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if len(sessions) <= 0:
            return None
        current_time = datetime.now()
        time_span = timedelta(seconds=self.session_duration)
        expire_time = sessions[0].created_at + time_span
        if expire_time < current_time:
            return None
        return sessions[0].user_id

    def destroy_session(self, request=None) -> bool:
        """Destroys an authenticated session.
        """
        session_id = self.session_cookie(request)
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if len(sessions) <= 0:
            return False
        sessions[0].remove()
        return True
