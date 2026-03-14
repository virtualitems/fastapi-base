#-*- coding: utf-8 -*-
"""Users module providers"""
from __future__ import annotations

from server.users.controllers import UsersController
from server.users.services import UsersService

user_service = UsersService()
user_controller = UsersController(service=user_service)

def provide_users_service() -> UsersService:
    """Provider for UsersService"""
    return user_service

def provide_users_controller() -> UsersController:
    """Provider for UsersController"""
    return user_controller
