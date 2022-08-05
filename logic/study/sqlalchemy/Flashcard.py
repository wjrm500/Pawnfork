from sqlalchemy import Column, ForeignKey, Integer, String

from logic.study.sqlalchemy import Base

class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key = True, autoincrement = True)
    deck_id = Column(Integer, ForeignKey('deck.id'))
    position = Column(String)
    opponents_move = Column(String)
    your_best_move = Column(String)