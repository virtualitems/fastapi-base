#-*- coding: utf-8 -*-
"""Users module ORM models"""
from __future__ import annotations

import hashlib
import hmac
import secrets

from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from server.shared.database.orm import BaseORM

class User(BaseORM):
    """ORM model for the User entity"""

    __tablename__ = 'auth_users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(300), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(300), nullable=False)
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    def set_password(self, password: str) -> None:
        """Creates a hash for the given password and stores it in the password field"""
        salt = secrets.token_hex(16)
        iterations = 600_000

        args = ('sha512', password.encode('utf-8'), salt.encode('utf-8'), iterations)
        pwd_hash = hashlib.pbkdf2_hmac(*args).hex()

        self.password = f'pbkdf2_sha512${iterations}${salt}${pwd_hash}'

    def verify_password(self, candidate_password: str) -> bool:
        """Verifies if the given password matches the stored hash"""

        if not isinstance(candidate_password, str) or candidate_password == '':
            return False

        algorithm, iterations_str, salt_hex, hash_hex = self.password.split('$')

        if algorithm != 'pbkdf2_sha512':
            return False

        try:
            iterations = int(iterations_str)
        except ValueError:
            return False

        salt = bytes.fromhex(salt_hex)
        stored_hash = bytes.fromhex(hash_hex)

        args = ('sha512', candidate_password.encode('utf-8'), salt, iterations)
        candidate_hash = hashlib.pbkdf2_hmac(*args)

        return hmac.compare_digest(candidate_hash, stored_hash)
