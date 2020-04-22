#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state')
    else:
        @property
        def cities(self):
            """
            Returns the list of City instances where
            state_id equals the current State.id
            """
            city_list = []
            city_dict = models.storage.all(City)
            for key, value in city_dict.items():
                if city_dict[key].state_id == self.id:
                    city_list.append(city_dict[key])
            return city_list
