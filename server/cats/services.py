#-*- coding: utf-8 -*-
"""Cats module services"""

from sqlalchemy.orm import Session
from server.cats.orms import Cat
from server.cats.dtos import CreateCatDTO

class CatsService:
    """Service layer for cats module"""

    def create_cat(self, db: Session, body: CreateCatDTO) -> Cat:
        """Create a new cat in the database"""
        cat = Cat(name=body.name)
        db.add(cat)
        db.commit()
        db.refresh(cat)
        return cat

    def list_cats(self, db: Session) -> list[Cat]:
        """List all cats in the database"""
        return db.query(Cat).all()
