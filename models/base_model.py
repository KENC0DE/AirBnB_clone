#!/usr/bin/python3
"""
### Base Model ###
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Initiation."""
        if kwargs != {}:
            del kwargs['__class__']
            for key, val in kwargs.items():
                self.__dict__[key] = val
            self.__dict__['created_at'] = datetime.fromisoformat(self.__dict__['created_at'])
            self.__dict__['updated_at'] = datetime.fromisoformat(self.__dict__['updated_at'])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Simple-Info"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save-Time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Model-dict """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        modict = {k: v for k, v in self.__dict__.items() if v is not None}
        modict["__class__"] = self.__class__.__name__
        return modict
