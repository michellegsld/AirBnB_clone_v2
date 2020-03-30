#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"), primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        __tablename__: table places
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column("city_id", String(60),
                     ForeignKey("cities.id"), nullable=False)
    user_id = Column("user_id", String(60),
                     ForeignKey("users.id"), nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024), nullable=True)
    number_rooms = Column("number_rooms", Integer, default=0, nullable=False)
    number_bathrooms = Column("number_bathrooms",
                              Integer, default=0, nullable=False)
    max_guest = Column("max_guest", Integer, default=0, nullable=False)
    price_by_night = Column("price_by_night",
                            Integer, default=0, nullable=False)
    latitude = Column("latitude", Float, nullable=True)
    longitude = Column("longitude", Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='place_amenities', viewonly=False)
    else:
        @property
        def reviews(self):
            """
            Returns the list of Review instances when place_id equals
            current Place.id
            """
            review_list = []
            review_dict = storage.all(Review)
            for key, value in review_dict.items():
                review_list.append(review_dict[key])
            return review_list

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """
            Handles append method for adding an Amenity.id to amenity_ids
            """
            if obj.id == Amenity.id:
                self.amenity_ids.append(obj)
