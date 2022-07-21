#!/usr/bin/env python3
from bcrypt import hashpw
import bcrypt
from typing import ByteString

def hash_password(password: str) -> ByteString:
    """
    Hash a password.
    """
    return hashpw(password.encode('utf-8'), bcrypt.gensalt())
