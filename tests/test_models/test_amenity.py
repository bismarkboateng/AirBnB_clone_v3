#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity
from os import getenv, remove


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestAmenity(unittest.TestCase):
<<<<<<< HEAD
    '''
        Testing Amenity class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_amenity = Amenity()
        cls.new_amenity.name = "wifi"
=======
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
>>>>>>> refs/remotes/origin/master

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_amenity
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

<<<<<<< HEAD
    def test_pep8_style_check(self):
        '''
            Tests pep8 style
        '''
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")
=======
    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)
>>>>>>> refs/remotes/origin/master

    def test_States_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_amenity.__tablename__, "amenities")

    def test_Amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        '''
            Test that Amenity class had name attribute.
        '''
        self.assertTrue("name" in self.new_amenity.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_Amenity_attribute_type(self):
        '''
            Test that Amenity class had name attribute's type.
        '''
        name_value = getattr(self.new_amenity, "name")
        self.assertIsInstance(name_value, str)
