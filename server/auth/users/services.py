#-*- coding: utf-8 -*-
"""Users module services"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from server.auth.users.orms import User
from server.auth.users.dtos import CreateUserDTO, UpdateUserDTO

class UsersService:
    """Service layer for users module"""

    def _generate_slug(self, email: str) -> str:
        """Generate a simple hash slug from email"""
        return hashlib.md5(email.encode()).hexdigest()

    def create_user(self, db: Session, body: CreateUserDTO) -> User:
        """Create a new user in the database"""
        existing_email = db.query(User).filter(User.email == body.email).first()

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email '{body.email}' already exists"
            )

        slug = self._generate_slug(body.email)
        jwt_version = int(datetime.now(timezone.utc).timestamp() * 1000)

        user = User(
            slug=slug,
            email=body.email,
            jwt_version=jwt_version,
            created_at=datetime.now(timezone.utc)
        )

        user.set_password(body.password)

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def list_users(self, db: Session) -> list[User]:
        """List all users in the database"""
        return db.query(User).filter(User.deleted_at.is_(None)).all()

    def get_user(self, db: Session, slug: str) -> User:
        """Get a user by slug"""
        user = db.query(User).filter(User.slug == slug, User.deleted_at.is_(None)).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with slug '{slug}' not found"
            )

        return user

    def update_user(self, db: Session, slug: str, body: UpdateUserDTO) -> User:
        """Update a user in the database"""
        user = self.get_user(db, slug)

        if body.email is None and body.password is None:
            return user

        if body.email is not None and body.email != user.email:
            existing = db.query(User).filter(User.email == body.email).first()

            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"User with email '{body.email}' already exists"
                )

            user.email = body.email
            user.slug = self._generate_slug(body.email)

        if body.password is not None:
            user.set_password(body.password)

        user.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, slug: str) -> None:
        """Soft delete a user (set deleted_at timestamp)"""
        user = self.get_user(db, slug)
        user.deleted_at = datetime.now(timezone.utc)
        db.commit()
