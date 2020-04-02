#!/usr/bin/python3
""" Tests for DBStorge """

import unittest
from models.engine.db_storage import DBStorage
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from sqlalchemy.sql import select


class TestDBStorage(unittest.TestCase):
    """ DBStorage Tests """

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """Tests all method """
        pass

    def test_new(self):
        """Tests new method """

        pass

    def test_delete(self):
        """Tests delete method """

        pass

    def test_reload(self):
        """Tests reload method """

        pass

    def test_place_amenity_table(self):
        """Tests place_amenity table """

        pass

    def test_column_cities(self):
        """Tests cities column  """

        pass

    def test_relationship_city_state(self):
        """Tests relationship between city and state """

        pass

    def test_drop(self):
        """Tests if all tables were dropped if HBNB_ENV == test """

        pass

    def test_relationship_place_user(self):
        """Tests relationship between place and user """

        pass

    def test_relationship_places_city(self):
        """Tests relationship between places and city"""

        pass
