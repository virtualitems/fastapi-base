#-*- coding: utf-8 -*-
"""Bootstrap the FastAPI server application."""

from fastapi import FastAPI

from server.cats.routes import router as cats_router
from server.container import InstancesContainer
from server.shared.env import Env

class FastAPIServer(FastAPI):
    """Main application class for the FastAPI server."""

    def __init__(self, *args, container, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = container

server = FastAPIServer(title=Env.get('APP_NAME'), container=InstancesContainer())

server.include_router(cats_router)
