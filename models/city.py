#!/usr/bin/python3
"""Defines the class city that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents the class city"""

    state_id = ""
    name = ""
