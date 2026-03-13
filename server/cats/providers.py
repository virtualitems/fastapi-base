#-*- coding: utf-8 -*-
"""Cats module providers"""
from __future__ import annotations

from server.cats.containers import Container
from server.cats.controllers import CatsController

container = Container()

def provide_cats_controller() -> CatsController:
    """Provider for CatsController"""
    return container.cats_controller()
