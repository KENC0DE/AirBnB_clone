#!/usr/bin/python3
"""
   Test storage File
"""
from unittest import TestCase
import pycodestyle
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """
    TestFileStorage class
    """

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.engine.file_storage').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = TestFileStorage.__doc__
        self.assertGreater(len(doc), 1)
