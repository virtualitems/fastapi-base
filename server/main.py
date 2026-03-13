#-*- coding: utf-8 -*-
"""Bootstrap the FastAPI server application."""
from __future__ import annotations

from fastapi import FastAPI

from server.cats.routes import router as cats_router
from server.users.routes import router as users_router
from server.shared.env import env

server = FastAPI(title=env.get('APP_NAME'))

server.include_router(cats_router)
server.include_router(users_router)
