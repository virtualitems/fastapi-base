#--*- coding: utf-8 -*-
"""Cats module controllers"""

from sqlalchemy.orm import Session
from server.cats.dtos import CreateCatDTO
from server.cats.services import CatsService


class CatsController:
    """Controller layer for cats module"""
    def __init__(self, service: CatsService):
        self.service = service

    def create(self, db: Session, body: CreateCatDTO):
        """Create a new cat"""
        return self.service.create_cat(db, body)

    def list(self, db: Session):
        """List all cats"""
        return self.service.list_cats(db)
