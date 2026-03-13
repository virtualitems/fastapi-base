#-*- coding: utf-8 -*-
"""Database models for the application"""
from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase

class BaseORM(DeclarativeBase):
    """Base class for all database models"""
