#!/usr/bin/python3
"""This database storage for AirBnB"""
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class will define how everything is saved in the database
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of db storage class
        """
        sql_user = getenv("HBNB_MYSQL_USER")
        sql_pass = getenv("HBNB_MYSQL_PWD")
        sql_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(sql_user, sql_pass,
                                              sql_host, db_name),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query either all of a certain type or every objects on
        the current database session
        """
        tables_list = [State, City, User, Amenity, Place, Review]
        query_list = []
        query_dict = {}

        if cls is None:
            for table in tables_list:
                query_list.append((self.__session).query(table).all())
            for query_table in query_list:
                for obj in query_table:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    query_dict[key] = obj
        else:
            query_list = (self.__session).query(cls).all()
            for obj in query_list:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                query_dict[key] = obj

        return query_dict

    def new(self, obj):
        """Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session if obj is not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and use sessionmaker
        """
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session
        """
        self.__session.close()
