#-*- coding: utf-8 -*-
"""Users module ORM models"""
from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from server.shared.database.orm import BaseORM

class User(BaseORM):
    """ORM model for the User entity"""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
