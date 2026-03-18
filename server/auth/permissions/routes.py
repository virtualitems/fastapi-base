#-*- coding: utf-8 -*-
"""Permissions module routes"""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.shared.database.providers import provide_database_session

from server.auth.permissions.services import PermissionsService
from server.auth.permissions.dtos import PermissionDTO
from server.auth.permissions.providers import provide_permissions_service

router = APIRouter(prefix='/permissions', tags=['permissions'])

@router.get('/', response_model=list[PermissionDTO])
def list_permissions(
    db: Session = Depends(provide_database_session),
    service: PermissionsService = Depends(provide_permissions_service)
):
    """Endpoint to list all permissions"""
    return service.list_permissions(db)


@router.get('/{slug}', response_model=PermissionDTO)
def get_permission(
    slug: str,
    db: Session = Depends(provide_database_session),
    service: PermissionsService = Depends(provide_permissions_service)
):
    """Endpoint to get a permission by slug"""
    return service.get_permission(db, slug)
