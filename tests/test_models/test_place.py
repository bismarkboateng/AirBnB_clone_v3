#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.place import Place
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestUser(unittest.TestCase):
    '''
        Testing Place class
    def test_pep8_style_check(self):
            Tests pep8 style
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/places.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")

    '''

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_place = Place(city_id="0O01", user_id="0O02", name="house",
                              description="awesome", number_rooms=3,
                              number_bathrooms=2, max_guest=1,
                              price_by_night=100, latitude=37.77,
                              longitude=127.12)

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_place
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_Place_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_place.__tablename__, "places")

    def test_Place_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''

        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        '''
            Checks that the attribute exist.
        '''
        self.assertTrue("city_id" in self.new_place.__dir__())
        self.assertTrue("user_id" in self.new_place.__dir__())
        self.assertTrue("description" in self.new_place.__dir__())
        self.assertTrue("name" in self.new_place.__dir__())
        self.assertTrue("number_rooms" in self.new_place.__dir__())
        self.assertTrue("max_guest" in self.new_place.__dir__())
        self.assertTrue("price_by_night" in self.new_place.__dir__())
        self.assertTrue("latitude" in self.new_place.__dir__())
        self.assertTrue("longitude" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_place_amenity_attrb(self):
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

<<<<<<< HEAD
    @unittest.skipIf(storage != "db", "Testing database storage only")
    def test_place_amenity_dbattrb(self):
        self.assertTrue("amenities" in self.new_place.__dir__())
        self.assertTrue("reviews" in self.new_place.__dir__())
=======
class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
>>>>>>> refs/remotes/origin/master

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_longitude(self):
        '''
            Test the type of longitude.
        '''
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_latitude(self):
        '''
            Test the type of latitude
        '''
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_amenity(self):
        '''
            Test the type of latitude
        '''
        amenity = getattr(self.new_place, "amenity_ids")
        self.assertIsInstance(amenity, list)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_price_by_night(self):
        '''
            Test the type of price_by_night
        '''
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_max_guest(self):
        '''
            Test the type of max_guest
        '''
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_bathrooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_rooms(self):
        '''
            Test the type of number_bathrooms
        '''
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_description(self):
        '''
            Test the type of description
        '''
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_user_id(self):
        '''
            Test the type of user_id
        '''
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

<<<<<<< HEAD
    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_city_id(self):
        '''
            Test the type of city_id
        '''
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
=======
    @unittest.skipIf(models.storage_t == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """Test Place has attr amenity_ids, and it's an empty list"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
>>>>>>> refs/remotes/origin/master
