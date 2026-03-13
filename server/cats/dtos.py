#-*- coding: utf-8 -*-
"""Cats module data models"""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class CreateCatDTO(BaseModel):
    """Data transfer object for creating a cat"""
    name: str = Field(min_length=1, max_length=100)

class CatDTO(BaseModel):
    """Data transfer object for a cat"""
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
