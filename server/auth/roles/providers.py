#-*- coding: utf-8 -*-
"""Roles module providers"""
from __future__ import annotations

from server.auth.roles.services import RolesService

roles_service = RolesService()

def provide_roles_service() -> RolesService:
    """Provider for RolesService"""
    return roles_service
