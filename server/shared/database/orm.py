#-*- coding: utf-8 -*-
"""Database models for the application"""

from sqlalchemy.orm import DeclarativeBase

class BaseORM(DeclarativeBase):
    """Base class for all database models"""
