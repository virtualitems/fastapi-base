#-*- coding: utf-8 -*-
"""Authentication module data models"""
from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field

class LoginDTO(BaseModel):
    """Data transfer object for login"""
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)

class TokenDTO(BaseModel):
    """Data transfer object for token response"""
    access_token: str
    token_type: str

class TokenDataDTO(BaseModel):
    """Data transfer object for token data"""
    sub: str | None = None
    ver: str | None = None
