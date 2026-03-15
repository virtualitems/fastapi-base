#-*- coding: utf-8 -*-
"""Environment variable loading for the application"""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import dotenv_values

def build_env(env_path: str | None = None, rules: dict | None = None) -> dict[str, str]:
    """Build the environment variable dictionary"""

    env_vars = dict(os.environ)

    if rules is None:
        rules = {}

    if isinstance(env_path, str) and Path(env_path).exists():
        env_vars.update(dotenv_values(env_path))

    for key, rules_list in rules.items():
        value = env_vars.get(key)

        for rule in rules_list:
            if rule(value) is False:
                msg = f'Environment variable {key} failed validation check: {rule.__name__}'
                raise EnvironmentError(msg)

    return env_vars

def exists(value: str) -> bool:
    """Check if an environment variable exists"""
    return value is not None

env = build_env(
    env_path=os.getenv('ENV_FILE'),
    rules={
        'APP_NAME': (exists, ),
        'DATABASE_URL': (exists, ),
    }
)
