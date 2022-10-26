#!/usr/bin/python3
'''
    Contain tests for the state module.
'''
import unittest
from models.base_model import BaseModel
from models.state import State
from os import getenv, remove
import pep8

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestState(unittest.TestCase):
<<<<<<< HEAD
    '''
        Test the State class.
    '''
=======
    """Test the State class"""

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
>>>>>>> refs/remotes/origin/master

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_state = State()
        cls.new_state.name = "California"

<<<<<<< HEAD
    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_state
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
=======
    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)
>>>>>>> refs/remotes/origin/master

    def test_States_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_state.__tablename__, "states")

    def test_State_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        self.assertIsInstance(self.new_state, BaseModel)

    def test_State_attributes(self):
        '''
            Test that State class contains the attribute `name`.
        '''
        self.assertTrue("name" in self.new_state.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_State_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        name = getattr(self.new_state, "name")
        self.assertIsInstance(name, str)
