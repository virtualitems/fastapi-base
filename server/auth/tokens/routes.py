#-*- coding: utf-8 -*-
"""Users module routes"""
from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix='/tokens', tags=['tokens'])
