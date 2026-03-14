#-*- coding: utf-8 -*-
"""Cats module providers"""
from __future__ import annotations

from server.cats.services import CatsService
from server.cats.controllers import CatsController

cats_service = CatsService()
cats_controller = CatsController(service=cats_service)

def provide_cats_service() -> CatsService:
    """Provider for CatsService"""
    return cats_service

def provide_cats_controller() -> CatsController:
    """Provider for CatsController"""
    return cats_controller
