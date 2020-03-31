#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
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
    cities = relationship('City', backref='state')

    @property
    def cities(self):
        """
        Returns the list of City instances where
        state_id equals the current State.id
        """
        city_list = []
        city_dict = storage.all(City)
        for key, value in city_dict.items():
            city_list.append(city_dict[key])
        return city_list
