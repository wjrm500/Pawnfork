from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy import Base

class StartPosition(Base):
    __tablename__ = 'start_position'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)

    ### One to many relationships
    decks = relationship('Deck', backref = 'start_position')
    moves = relationship('StartPositionMove', backref = 'start_position')