#-*- coding: utf-8 -*-
"""Environment variable loading for the application"""
from __future__ import annotations

from os import getenv
from pathlib import Path

from dotenv import dotenv_values

env: dict[str, str] = dotenv_values('.env') if Path('.env').exists() else {}

env_vars = [
    'APP_NAME',
    'DATABASE_URL',
]

for key in env_vars:
    value = env.get(key)

    if value is None:
        value = getenv(key)
        env[key] = value

    if value is None:
        raise EnvironmentError(f'Missing required environment variable: {key}')
