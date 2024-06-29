#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, CheckConstraint


class Review(BaseModel, Base):
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        body = Column(String(1024), nullable=False)
        rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False)
        
    else:
        place_id = ""
        user_id = ""
        body = ""
        rating = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
