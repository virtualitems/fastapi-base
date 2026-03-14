#-*- coding: utf-8 -*-
"""Users module services"""
from __future__ import annotations

from sqlalchemy.orm import Session
from server.auth.users.orms import User
from server.auth.users.dtos import CreateUserDTO

class UsersService:
    """Service layer for users module"""

    def create_user(self, db: Session, body: CreateUserDTO) -> User:
        """Create a new user in the database"""
        user = User(name=body.name)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def list_users(self, db: Session) -> list[User]:
        """List all users in the database"""
        return db.query(User).all()
