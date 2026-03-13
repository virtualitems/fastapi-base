#-*- coding: utf-8 -*-
"""Cats module services"""

from sqlalchemy.orm import Session
from server.cats.orms import Cat
from server.cats.dtos import CreateCatDTO

class CatsService:
    """Service layer for cats module"""
    def __init__(self, db: Session):
        self.db = db

    def create_cat(self, body: CreateCatDTO) -> Cat:
        """Create a new cat in the database"""
        cat = Cat(name=body.name)
        self.db.add(cat)
        self.db.commit()
        self.db.refresh(cat)
        return cat

    def list_cats(self) -> list[Cat]:
        """List all cats in the database"""
        return self.db.query(Cat).all()
