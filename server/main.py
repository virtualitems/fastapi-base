#-*- coding: utf-8 -*-
"""Bootstrap the FastAPI server application."""

from fastapi import FastAPI

from server.cats.routes import router as cats_router
from server.shared.env import Env

server = FastAPI(title=Env.get('APP_NAME'))

server.include_router(cats_router)
