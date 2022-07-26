#!/usr/bin/env python3
""" 6. Basic auth"""
import base64
import email

from click import password_option
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        return: the decoded Base64 part of the Authorization header
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        if base64_authorization_header != base64_authorization_header.encode():

            try:
                return base64.b64decode(
                    base64_authorization_header).decode('utf-8')
            except Exception:
                return None

        return base64_authorization_header.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_credentials = decoded_base64_authorization_header.split(':')
        if len(user_credentials) != 2:
            return None, None
        return user_credentials[0], user_credentials[1]
