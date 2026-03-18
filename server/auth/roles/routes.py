#-*- coding: utf-8 -*-
"""Roles module routes"""
from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from server.shared.database.providers import provide_database_session

from server.auth.roles.services import RolesService
from server.auth.roles.dtos import CreateRoleDTO, UpdateRoleDTO, RoleDTO
from server.auth.roles.providers import provide_roles_service

router = APIRouter(prefix='/roles', tags=['roles'])

@router.post('/', response_model=RoleDTO, status_code=status.HTTP_201_CREATED)
def create_role(
    body: CreateRoleDTO,
    db: Session = Depends(provide_database_session),
    service: RolesService = Depends(provide_roles_service)
):
    """Endpoint to create a new role"""
    return service.create_role(db, body)


@router.get('/', response_model=list[RoleDTO])
def list_roles(
    db: Session = Depends(provide_database_session),
    service: RolesService = Depends(provide_roles_service)
):
    """Endpoint to list all roles"""
    return service.list_roles(db)


@router.get('/{slug}', response_model=RoleDTO)
def get_role(
    slug: str,
    db: Session = Depends(provide_database_session),
    service: RolesService = Depends(provide_roles_service)
):
    """Endpoint to get a role by slug"""
    return service.get_role(db, slug)


@router.put('/{slug}', response_model=RoleDTO)
def update_role(
    slug: str,
    body: UpdateRoleDTO,
    db: Session = Depends(provide_database_session),
    service: RolesService = Depends(provide_roles_service)
):
    """Endpoint to update a role"""
    return service.update_role(db, slug, body)


@router.delete('/{slug}', status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
    slug: str,
    db: Session = Depends(provide_database_session),
    service: RolesService = Depends(provide_roles_service)
):
    """Endpoint to delete a role"""
    service.delete_role(db, slug)
