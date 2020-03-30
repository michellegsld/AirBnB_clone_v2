#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        __tablename__ : users table
        email: email address
        password: password for your login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column("email", String(128), nullable=False)
    password = Column("password", String(128), nullable=False)
    first_name = Column("first_name", String(128), nullable=True)
    last_name = Column("last_name", String(128), nullable=True)
    places = relationship('Place', backref='user')
    reviews = relationship('Review', backref='user')
