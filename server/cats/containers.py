# -*- coding: utf-8 -*-
"""Cats module dependencies container"""
from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Configuration

from server.cats.controllers import CatsController
from server.cats.services import CatsService

class Container(DeclarativeContainer):
    config = Configuration()
    cats_service = Singleton(CatsService)
    cats_controller = Singleton(CatsController, service=cats_service)
