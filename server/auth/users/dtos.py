#-*- coding: utf-8 -*-
"""Users module data models"""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class CreateUserDTO(BaseModel):
    """Data transfer object for creating a user"""
    email: EmailStr = Field(description="User email address")
    password: str = Field(min_length=8, max_length=100, description="User password")

class UserDTO(BaseModel):
    """Data transfer object for a user"""
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: str
