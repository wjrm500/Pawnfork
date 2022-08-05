from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy import Base

class Deck(Base):
    __tablename__ = 'deck'

    id = Column(Integer, primary_key = True, autoincrement = True)
    start_position = Column(String)
    player_colour = Column(String)

    ### One to many relationships
    flashcards = relationship('Flashcard', backref = 'deck')