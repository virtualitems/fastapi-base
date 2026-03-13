#-*- coding: utf-8 -*-
"""Database providers for the application"""

from __future__ import annotations

from sqlalchemy import create_engine, orm

from server.shared.env import Env

engine = create_engine(
    url=Env.get('DATABASE_URL'),
    connect_args={"check_same_thread": False},
)

SessionLocal = orm.sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

def provide_database_session():
    """Provides a database session"""
    db: orm.Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
