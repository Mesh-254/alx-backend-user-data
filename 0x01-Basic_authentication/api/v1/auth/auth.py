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
        #this method must be slash tolerant (/) or not (not/) slash at the end of the path 
        if path[-1] == "/" or path[-1] == "not/":
            if excluded_paths[-1] == "/":
                return False
        

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
