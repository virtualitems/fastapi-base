#-*- coding: utf-8 -*-
"""Users module data models"""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class CreateUserDTO(BaseModel):
    """Data transfer object for creating a user"""
    name: str = Field(min_length=1, max_length=100)

class UserDTO(BaseModel):
    """Data transfer object for a user"""
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
