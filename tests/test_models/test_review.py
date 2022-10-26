#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
import pep8
from models.base_model import BaseModel
from models.review import Review
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestReview(unittest.TestCase):
<<<<<<< HEAD
    '''
        Testing Review class
    '''
=======
    """Test the Review class"""

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
>>>>>>> refs/remotes/origin/master

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.rev = Review()
        cls.rev.user_id = "Adriel and Melissa 123"
        cls.rev.place_id = "Amy and Victor's room at SF"
        cls.rev.text = "Team Awesome includes Adekunle"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.rev
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_style_check(self):
        '''
            Tests pep8 style
        '''
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")

<<<<<<< HEAD
    def test_Review_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.rev.__tablename__, "reviews")
=======
    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)
>>>>>>> refs/remotes/origin/master

    def test_Review_inheritance(self):
        '''
            Tests that the Review class Inherits from BaseModel
        '''
        self.assertIsInstance(self.rev, BaseModel)

    def test_Review_attributes(self):
        '''
            Tests Review class has place_id, user_id and text attributes
        '''
        self.assertTrue("place_id" in self.rev.__dir__())
        self.assertTrue("user_id" in self.rev.__dir__())
        self.assertTrue("text" in self.rev.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        place_id = getattr(self.rev, "place_id")
        user_id = getattr(self.rev, "user_id")
        text = getattr(self.rev, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
