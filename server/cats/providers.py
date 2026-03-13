#-*- coding: utf-8 -*-
"""Cats module providers"""

from fastapi import Depends
from sqlalchemy.orm import Session

from server.shared.database.providers import provide_database_session
from server.cats.controllers import CatsController
from server.cats.services import CatsService

def provide_cats_service(db: Session = Depends(provide_database_session)) -> CatsService:
    """Provides an instance of CatsService with a database session dependency"""
    return CatsService(db=db)


def provide_cats_controller(service: CatsService = Depends(provide_cats_service)) -> CatsController:
    """Provides an instance of CatsController with a CatsService dependency"""
    return CatsController(service=service)
