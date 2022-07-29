#!/usr/bin/env python3
"""python class Auth"""
from typing import List, TypeVar
from flask import request


class Auth:
    """class Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method require authentication"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False

        if path[-1] != '/' and path + '/'\
                in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method
        authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """method to access current user"""
        return None

    def session_cookie(self, request=None):
        """
        get the session cookie
        :param request:
        :return: cookie
        """
        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        session_id = request.cookies.get(SESSION_NAME)

        return
