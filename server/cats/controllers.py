#--*- coding: utf-8 -*-
"""Cats module controllers"""

from server.cats.dtos import CreateCatDTO
from server.cats.services import CatsService


class CatsController:
    """Controller layer for cats module"""
    def __init__(self, service: CatsService):
        self.service = service

    def create(self, body: CreateCatDTO):
        """Create a new cat"""
        return self.service.create_cat(body)

    def list(self):
        """List all cats"""
        return self.service.list_cats()
