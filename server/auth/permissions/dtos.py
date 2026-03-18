#-*- coding: utf-8 -*-
"""Permissions module data models"""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict

class PermissionDTO(BaseModel):
    """Data transfer object for a permission"""
    model_config = ConfigDict(from_attributes=True)
    slug: str
    description: str
