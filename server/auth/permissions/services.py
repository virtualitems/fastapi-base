#-*- coding: utf-8 -*-
"""Permissions module services"""
from __future__ import annotations

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from server.auth.permissions.orms import Permission

class PermissionsService:
    """Service layer for permissions module"""

    def list_permissions(self, db: Session) -> list[Permission]:
        """List all permissions in the database"""
        return db.query(Permission).filter(Permission.deleted_at.is_(None)).all()

    def get_permission(self, db: Session, slug: str) -> Permission:
        """Get a permission by slug"""
        permission = db.query(Permission).filter(
            Permission.slug == slug,
            Permission.deleted_at.is_(None)
        ).first()
        if not permission:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Permission with slug '{slug}' not found"
            )
        return permission
