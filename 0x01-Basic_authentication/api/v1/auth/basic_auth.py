#!/usr/bin/env python3
""" 6. Basic auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        :param authorization_header: the Authorization header
        :return: the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if (authorization_header.startswith('Basic ')) is False:
            return None

        return authorization_header.split(' ')[-1]
