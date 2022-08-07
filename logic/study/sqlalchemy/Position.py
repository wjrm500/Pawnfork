from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy import Base

class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)

    ### One to many relationships
    decks = relationship('Deck', backref = 'position')
    flashcards = relationship('Flashcard', backref = 'position')
    moves = relationship('PositionMove', backref = 'position')