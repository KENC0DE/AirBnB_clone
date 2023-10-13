#!/usr/bin/python3
"""
### Base Model ###
"""


import uuid
import datetime


class BaseModel:
    """ Base Model Class"""

    def __init__(self):
        """Initiation."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Simple-Info"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save-Time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Model-dict """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        modict = {k: v for k, v in self.__dict__.items() if v is not None}
        modict["__class__"] = self.__class__.__name__
        return modict
