#-*- coding: utf-8 -*-
"""Cats module routes"""
from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from server.cats.controllers import CatsController
from server.cats.dtos import CreateCatDTO, CatDTO
from server.cats.providers import provide_cats_controller
from server.shared.database.providers import provide_database_session

router = APIRouter(prefix='/cats', tags=['cats'])

@router.post('/', response_model=CatDTO, status_code=status.HTTP_201_CREATED)
def create_cat(
    body: CreateCatDTO,
    db: Session = Depends(provide_database_session),
    controller: CatsController = Depends(provide_cats_controller)
):
    """Endpoint to create a new cat"""
    return controller.create(db, body)


@router.get('/', response_model=list[CatDTO])
def list_cats(
    db: Session = Depends(provide_database_session),
    controller: CatsController = Depends(provide_cats_controller)
):
    """Endpoint to list all cats"""
    return controller.list(db)
