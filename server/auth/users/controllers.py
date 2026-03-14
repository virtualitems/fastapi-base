#--*- coding: utf-8 -*-
"""Users module controllers"""
from __future__ import annotations

from sqlalchemy.orm import Session
from server.auth.users.dtos import CreateUserDTO
from server.auth.users.services import UsersService


class UsersController:
    """Controller layer for users module"""
    def __init__(self, service: UsersService):
        self.service = service

    def create(self, db: Session, body: CreateUserDTO):
        """Create a new user"""
        return self.service.create_user(db, body)

    def list(self, db: Session):
        """List all users"""
        return self.service.list_users(db)
