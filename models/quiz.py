#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Text, Table
from sqlalchemy.orm import relationship





class Quiz(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'quizzes'
        title = Column(String(128), nullable=False)
        description = Column(Text, nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        
        quizzes_questions = relationship("Quiz_Questions", backref="quiz_questions", cascade="all, delete")

    else:
        user_id = ""
        title = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes question"""
        super().__init__(*args, **kwargs)
