#-*- coding: utf-8 -*-
"""Roles module data models"""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

class CreateRoleDTO(BaseModel):
    """Data transfer object for creating a role"""
    description: str = Field(min_length=1, max_length=500)

class UpdateRoleDTO(BaseModel):
    """Data transfer object for updating a role"""
    description: Optional[str] = Field(None, min_length=1, max_length=500)

class RoleDTO(BaseModel):
    """Data transfer object for a role"""
    model_config = ConfigDict(from_attributes=True)
    slug: str
    description: str
