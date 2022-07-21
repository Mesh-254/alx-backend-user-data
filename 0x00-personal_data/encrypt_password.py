#!/usr/bin/env python3
from bcrypt import hashpw
import bcrypt


def hash_password(password: str) -> str:
    """
    Hash a password.
    """
    return hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
