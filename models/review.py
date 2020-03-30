#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        __tablename__: table reviews
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = Column("text", String(1024), nullable=False)
    place_id = Column("place_id", String(60),
                      ForeignKey("places.id"), nullable=False)
    user_id = Column("user_id", String(60),
                     ForeignKey("users.id"), nullable=False)
