#-*- coding: utf-8 -*-
"""Shared response models for API endpoints"""
from __future__ import annotations

from pydantic import BaseModel

class BaseResponse(BaseModel):
    """Base response model for API responses"""
    messages: list[str]
    data: dict | list | None = None
