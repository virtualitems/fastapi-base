#-*- coding: utf-8 -*-
"""Users module providers"""
from __future__ import annotations

from server.users.containers import Container
from server.users.controllers import UsersController

container = Container()

def provide_users_controller() -> UsersController:
    """Provider for UsersController"""
    return container.users_controller()
