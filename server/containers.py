#-*- coding: utf-8 -*-

from dependency_injector import containers


class InstancesContainer(containers.DeclarativeContainer):
    """Dependency injection container for the application."""

    wiring_config = containers.WiringConfiguration()
