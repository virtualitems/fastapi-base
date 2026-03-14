#-*- coding: utf-8 -*-
"""Users module routes"""
from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from server.shared.database.providers import provide_database_session

from server.users.controllers import UsersController
from server.users.dtos import CreateUserDTO, UserDTO
from server.users.providers import provide_users_controller

router = APIRouter(prefix='/users', tags=['users'])

@router.post('/', response_model=UserDTO, status_code=status.HTTP_201_CREATED)
def create_user(
    body: CreateUserDTO,
    db: Session = Depends(provide_database_session),
    controller: UsersController = Depends(provide_users_controller)
):
    """Endpoint to create a new user"""
    return controller.create(db, body)


@router.get('/', response_model=list[UserDTO])
def list_users(
    db: Session = Depends(provide_database_session),
    controller: UsersController = Depends(provide_users_controller)
):
    """Endpoint to list all users"""
    return controller.list(db)
