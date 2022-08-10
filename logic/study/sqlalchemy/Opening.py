from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy import Base

class Opening(Base):
    __tablename__ = 'opening'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)

    ### One to many relationships
    decks = relationship('Deck', backref = 'opening', cascade = 'all,delete')
    moves = relationship('OpeningMove', backref = 'opening', cascade = 'all,delete')