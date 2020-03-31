#!/usr/bin/python3
""" Tests for DBStorge """

import unittest
from models.engine.db_storage import DBStorage
import os
from sqlalchemy.sql import select


class TestDBStorage(unittest.TestCase):
    """ DBStorage Tests """

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_all(self):
        """Tests all method """
        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_new(self):
        """Tests new method """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_delete(self):
        """Tests delete method """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_reload(self):
        """Tests reload method """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_place_amenity_table(self):
        """Tests place_amenity table """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_column_cities(self):
        """Tests cities column  """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_relationship_city_state(self):
        """Tests relationship between city and state """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_drop(self):
        """Tests if all tables were dropped if HBNB_ENV == test """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_relationship_place_user(self):
        """Tests relationship between place and user """

        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !=
                     'db', "Incorrect storage type")
    def test_relationship_places_city(self):
        """Tests relationship between places and city"""

        pass

if __name__ == "__main__":
    unittest.main()
