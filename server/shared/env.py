#-*- coding: utf-8 -*-
"""Environment variable loading for the application"""
from __future__ import annotations

from os import getenv
from pathlib import Path

from dotenv import dotenv_values

def exists(value: str) -> bool:
    """Check if an environment variable exists"""
    return value is not None

def build_env():
    """Build the environment variable dictionary"""

    rules = {
        'APP_NAME': (exists, ),
        'DATABASE_URL': (exists, ),
    }

    env_vars = {}

    if Path('.env').exists():
        env_vars.update(dotenv_values('.env'))

    for key, rules in rules.items():
        value = env_vars.get(key)

        if value is None:
            value = getenv(key)
            env_vars[key] = value

        for rule in rules:
            if not rule(value):
                raise EnvironmentError(f'Environment variable {key} failed validation check: {rule.__name__}')

        env_vars[key] = value

    return env_vars

env = build_env()
