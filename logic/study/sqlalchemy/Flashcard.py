from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy import Base

class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key = True, autoincrement = True)
    deck_id = Column(Integer, ForeignKey('deck.id'))
    your_best_move = Column(String)

    ### One to many relationships
    moves = relationship('FlashcardMove', backref = 'flashcard')

    def opponents_move(self) -> str:
        return self.moves[-1]