#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        __tablename__: table Amenities
        name: input name
    """
    __tablename__ = "amenities"
    name = Column("name", String(128), nullable=False)
