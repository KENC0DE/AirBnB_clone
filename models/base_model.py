#!/usr/bin/python3
"""
### Base Model ###
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Initiation."""
        if kwargs is not None and kwargs != {}:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Simple-Info"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save-Time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Model-dict """
        custom_dict = self.__dict__.copy()
        custom_dict['__class__'] = self.__class__.__name__
        custom_dict['created_at'] = custom_dict['created_at'].isoformat()
        custom_dict['updated_at'] = custom_dict['updated_at'].isoformat()
        return custom_dict
