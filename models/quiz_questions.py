
#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Text, Table
from sqlalchemy.orm import relationship


# CREATE TABLE questions (
#     question_id INT AUTO_INCREMENT PRIMARY KEY,
#     quiz_id INT,
#     question_text TEXT NOT NULL,
#     FOREIGN KEY (quiz_id) REFERENCES quizzes(quiz_id) ON DELETE CASCADE
# );



class Quiz_Questions(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'quizzes_questions'
        quiz_id = Column(String(60), ForeignKey('quizzes.id'), nullable=False)
        question_text = Column(Text, nullable=False)
        correct_answer = Column(Text, nullable=False)
        quiz_questions_choices = relationship("Quiz_Questions_Choices", backref="quiz_questions_choices", cascade="all, delete")
        
    else:
        quiz_id = ""
        question_text = ""

    def __init__(self, *args, **kwargs):
        """initializes question"""
        super().__init__(*args, **kwargs)

