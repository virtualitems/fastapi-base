#-*- coding: utf-8 -*-
"""Bootstrap the FastAPI server application."""
from __future__ import annotations

from fastapi import FastAPI, status

from server.auth.tokens.routes import router as tokens_router
from server.auth.users.routes import router as users_router
from server.shared.env import env

server = FastAPI(title=env.get('APP_NAME'))

@server.get('/health', status_code=status.HTTP_204_NO_CONTENT)
def health_check():
    """Endpoint to check the health of the server"""

server.include_router(tokens_router, prefix='/api')
server.include_router(users_router, prefix='/api')
