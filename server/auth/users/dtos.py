#-*- coding: utf-8 -*-
"""Users module data models"""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class CreateUserDTO(BaseModel):
    """Data transfer object for creating a user"""
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)

class UpdateUserDTO(BaseModel):
    """Data transfer object for updating a user"""
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8, max_length=100)

class UserDTO(BaseModel):
    """Data transfer object for a user"""
    model_config = ConfigDict(from_attributes=True)
    slug: str
    email: str
    last_login: Optional[datetime]
