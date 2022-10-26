#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_city = City()
        cls.new_city.state_id = "California"
        cls.new_city.name_id = "San Francisco"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_city
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_City_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_city.__tablename__, "cities")

    def test_City_inheritance(self):
        '''
            Tests that the City class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_city, BaseModel)

    def test_User_attributes(self):
        '''
            Test user attributes exist
        '''
        self.assertTrue("state_id" in self.new_city.__dir__())
        self.assertTrue("name" in self.new_city.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "name")
        self.assertIsInstance(name, str)

<<<<<<< HEAD
    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "state_id")
        self.assertIsInstance(name, str)
=======

class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        if models.storage_t == 'db':
            self.assertEqual(city.name, None)
        else:
            self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        if models.storage_t == 'db':
            self.assertEqual(city.state_id, None)
        else:
            self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
>>>>>>> refs/remotes/origin/master
