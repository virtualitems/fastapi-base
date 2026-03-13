# -*- coding: utf-8 -*-
"""Users module dependencies container"""
from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Configuration

from server.users.controllers import UsersController
from server.users.services import UsersService

class Container(DeclarativeContainer):
    """Dependency injection container for users module"""
    config = Configuration()
    users_service = Singleton(UsersService)
    users_controller = Singleton(UsersController, service=users_service)
