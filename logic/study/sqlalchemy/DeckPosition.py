from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy import Base

class DeckPosition(Base):
    __tablename__ = 'deck_position'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)

    ### One to many relationships
    decks = relationship('Deck', backref = 'deck_position')
    moves = relationship('DeckPositionMove', backref = 'deck_position')