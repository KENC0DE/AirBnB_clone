#!/usr/bin/python3
"""
    Test Base Model
"""


import unittest
import pycodestyle
import uuid
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests Base Model"""

    def test_style(self):
        """test pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py',
                                    'tests/test_models/test_BaseModel.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
