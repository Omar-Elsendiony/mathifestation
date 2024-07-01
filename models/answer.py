#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Text, Table
from sqlalchemy.orm import relationship





class Answer(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'answers'
        question_id = Column(String(60), ForeignKey('questions.id'))
        user_id = Column(String(60), ForeignKey('users.id'))
        body = Column(Text, nullable=False)
        
        # questions_answers = relationship("Question", backref="answers" , foreign_keys=[question_id])
        # users_answers = relationship("User", backref="answers", foreign_keys=[user_id])
        
        
    else:
        question_id = ""
        user_id = ""
        body = ""

    def __init__(self, *args, **kwargs):
        """initializes answer"""
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
