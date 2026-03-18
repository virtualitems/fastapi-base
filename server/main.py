#-*- coding: utf-8 -*-
"""Bootstrap the FastAPI server application."""
from __future__ import annotations

from fastapi import FastAPI, status

from server.shared.env import env

from server.auth.permissions.routes import router as permissions_router
from server.auth.roles.routes import router as roles_router
from server.auth.users.routes import router as users_router

server = FastAPI(title=env.get('APP_NAME'))

@server.get('/api/health', status_code=status.HTTP_204_NO_CONTENT)
def health_check():
    """Endpoint to check the health of the server"""

server.include_router(users_router, prefix='/api')
server.include_router(roles_router, prefix='/api')
server.include_router(permissions_router, prefix='/api')
