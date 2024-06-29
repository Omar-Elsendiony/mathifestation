#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Text, Table
from sqlalchemy.orm import relationship





class Question(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'questions'
        # answer_id = Column(Integer, ForeignKey('answers.id'))
        user_id = Column(Integer, ForeignKey('users.id'))
        title = Column(String(128), nullable=False)
        body = Column(Text, nullable=False)
        answer = relationship("Answer", backref="answers")
        # user = relationship("User", backref="answers")
        
        
    else:
        user_id = ""
        title = ""
        body = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    # if models.storage_t != "db":
    #     @property
    #     def cities(self):
    #         """getter for list of city instances related to the state"""
    #         city_list = []
    #         all_cities = models.storage.all(City)
    #         for city in all_cities.values():
    #             if city.state_id == self.id:
    #                 city_list.append(city)
    #         return city_list
