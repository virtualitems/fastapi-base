#-*- coding: utf-8 -*-
"""Roles module services"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from server.auth.roles.orms import Role
from server.auth.roles.dtos import CreateRoleDTO, UpdateRoleDTO

class RolesService:
    """Service layer for roles module"""

    def _generate_slug(self, description: str) -> str:
        """Generate a simple hash slug from description"""
        return hashlib.md5(description.encode()).hexdigest()

    def create_role(self, db: Session, body: CreateRoleDTO) -> Role:
        """Create a new role in the database"""
        # Generate slug from description
        slug = self._generate_slug(body.description)

        # Check if slug already exists
        existing = db.query(Role).filter(Role.slug == slug).first()

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Role with this description already exists"
            )

        role = Role(
            slug=slug,
            description=body.description,
            created_at=datetime.now(timezone.utc)
        )

        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def list_roles(self, db: Session) -> list[Role]:
        """List all roles in the database"""
        return db.query(Role).filter(Role.deleted_at.is_(None)).all()

    def get_role(self, db: Session, slug: str) -> Role:
        """Get a role by slug"""
        role = db.query(Role).filter(Role.slug == slug, Role.deleted_at.is_(None)).first()

        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Role with slug '{slug}' not found"
            )
        return role

    def update_role(self, db: Session, slug: str, body: UpdateRoleDTO) -> Role:
        """Update a role in the database"""
        role = self.get_role(db, slug)

        if not body.description:
            return role

        new_slug = self._generate_slug(body.description)

        if new_slug != role.slug:
            existing = db.query(Role).filter(Role.slug == new_slug).first()
            if existing:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Role with this description already exists"
                )
            role.slug = new_slug

        role.description = body.description
        role.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(role)
        return role

    def delete_role(self, db: Session, slug: str) -> None:
        """Soft delete a role (set deleted_at timestamp)"""
        role = self.get_role(db, slug)
        role.deleted_at = datetime.now(timezone.utc)
        db.commit()
