#-*- coding: utf-8 -*-
"""Users module routes"""
from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from server.shared.database.providers import provide_database_session

from server.auth.users.services import UsersService
from server.auth.users.dtos import CreateUserDTO, UpdateUserDTO, UserDTO
from server.auth.users.providers import provide_users_service

router = APIRouter(prefix='/users', tags=['users'])

@router.post('/', response_model=UserDTO, status_code=status.HTTP_201_CREATED)
def create_user(
    body: CreateUserDTO,
    db: Session = Depends(provide_database_session),
    service: UsersService = Depends(provide_users_service)
):
    """Endpoint to create a new user"""
    return service.create_user(db, body)


@router.get('/', response_model=list[UserDTO])
def list_users(
    db: Session = Depends(provide_database_session),
    service: UsersService = Depends(provide_users_service)
):
    """Endpoint to list all users"""
    return service.list_users(db)


@router.get('/{slug}', response_model=UserDTO)
def get_user(
    slug: str,
    db: Session = Depends(provide_database_session),
    service: UsersService = Depends(provide_users_service)
):
    """Endpoint to get a user by slug"""
    return service.get_user(db, slug)


@router.put('/{slug}', response_model=UserDTO)
def update_user(
    slug: str,
    body: UpdateUserDTO,
    db: Session = Depends(provide_database_session),
    service: UsersService = Depends(provide_users_service)
):
    """Endpoint to update a user"""
    return service.update_user(db, slug, body)


@router.delete('/{slug}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    slug: str,
    db: Session = Depends(provide_database_session),
    service: UsersService = Depends(provide_users_service)
):
    """Endpoint to delete a user"""
    service.delete_user(db, slug)
