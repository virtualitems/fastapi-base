#-*- coding: utf-8 -*-
"""Users module providers"""
from __future__ import annotations

from server.auth.users.services import UsersService

users_service = UsersService()

def provide_users_service() -> UsersService:
    """Provider for UsersService"""
    return users_service
