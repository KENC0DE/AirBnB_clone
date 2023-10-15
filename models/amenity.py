#!/usr/bin/python3
"""
    Amenity File
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """ Overide Amenity init"""
        super().__init__(*args, **kwargs)
