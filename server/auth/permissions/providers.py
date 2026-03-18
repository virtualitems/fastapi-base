#-*- coding: utf-8 -*-
"""Permissions module providers"""
from __future__ import annotations

from server.auth.permissions.services import PermissionsService

permission_service = PermissionsService()

def provide_permissions_service() -> PermissionsService:
    """Provider for PermissionsService"""
    return permission_service
