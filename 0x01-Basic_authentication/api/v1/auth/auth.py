#!/usr/bin/env python3
"""python class Auth"""
import re
from typing import TypeVar
from flask import List


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
        if path == "/api/v1/status/" and excluded_paths == ["/api/v1/status/"]:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method
        authorization header
        """
        if request is None:
            return None
        if request["Authorization"] is None:
            return None
        return request["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """method to access current user"""
        return None
