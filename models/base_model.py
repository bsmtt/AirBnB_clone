#!/usr/bin/python3
"""the Base Model """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the BaseModel of HBnB """

    def __init__(self):
        """Initialize BaseModel."""

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


