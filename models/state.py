#!/usr/bin/python3
"""
    State File
"""


from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """ Overide State init"""
        super().__init__(*args, **kwargs)
