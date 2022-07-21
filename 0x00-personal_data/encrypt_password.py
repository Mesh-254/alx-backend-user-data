#!/usr/bin/env python3

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
