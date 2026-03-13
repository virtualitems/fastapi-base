#-*- coding: utf-8 -*-
"""Cats module routes"""

from __future__ import annotations

from fastapi import APIRouter, Depends, status

from server.cats.models import CatDTO, CreateCatDTO
from server.cats.controllers import CatsController
from server.cats.providers import provide_cats_controller

router = APIRouter(prefix='/cats', tags=['cats'])

@router.post('/', response_model=CatDTO, status_code=status.HTTP_201_CREATED)
def create_cat(body: CreateCatDTO, controller: CatsController = Depends(provide_cats_controller)):
    """Endpoint to create a new cat"""
    return controller.create(body)


@router.get('/', response_model=list[CatDTO])
def list_cats(controller: CatsController = Depends(provide_cats_controller)):
    """Endpoint to list all cats"""
    return controller.list()
