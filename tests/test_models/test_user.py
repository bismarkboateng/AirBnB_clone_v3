#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.user import User
from os import getenv, remove
from io import StringIO
import sys
import datetime
import pep8


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestUser(unittest.TestCase):
<<<<<<< HEAD
    '''
        Testing User class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_user = User()
        cls.new_user.email = "email@gmail.com"
        cls.new_user.password = "password"
        cls.new_user.firt_name = "Mel"
        cls.new_user.last_name = "Ng"
=======
    """Test the User class"""

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
>>>>>>> refs/remotes/origin/master

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_user
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_User_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_user.__tablename__, "users")

    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_user, BaseModel)

    def test_User_attributes(self):
        '''
            Test the user attributes exist
        '''
        self.assertTrue("email" in self.new_user.__dir__())
        self.assertTrue("first_name" in self.new_user.__dir__())
        self.assertTrue("last_name" in self.new_user.__dir__())
        self.assertTrue("password" in self.new_user.__dir__())

<<<<<<< HEAD
    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_email(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_user, "email")
        self.assertIsInstance(name, str)
=======
    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)
>>>>>>> refs/remotes/origin/master

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_first_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_user, "first_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_last_name(self):
        '''
            Test the type of last_name
        '''
        name = getattr(self.new_user, "last_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_password(self):
        '''
            Test the type of password
        '''
        name = getattr(self.new_user, "password")
        self.assertIsInstance(name, str)
