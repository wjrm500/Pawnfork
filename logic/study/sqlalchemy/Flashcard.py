from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy import Base

class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key = True, autoincrement = True)
    deck_id = Column(Integer, ForeignKey('deck.id'))
    best_move = Column(String)
    algebraic_best_move = Column(String)
    algebraic_opponents_move = Column(String)

    ### One to many relationships
    moves = relationship('FlashcardMove', backref = 'flashcard', cascade = 'all,delete')