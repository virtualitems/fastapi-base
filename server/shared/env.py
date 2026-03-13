#-*- coding: utf-8 -*-
"""Environment variable loading for the application"""
from __future__ import annotations

from os import getenv

from dotenv import load_dotenv

load_dotenv()

class Env:
    """Environment variable access class"""

    @staticmethod
    def get(key: str, default: str = None) -> str:
        """Get an environment variable value"""
        return getenv(key, default)
