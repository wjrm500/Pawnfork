import random
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy.Flashcard import Flashcard
from logic.study.sqlalchemy import Base

class Deck(Base):
    __tablename__ = 'deck'

    id = Column(Integer, primary_key = True, autoincrement = True)
    start_position_id = Column(Integer, ForeignKey('start_position.id'))
    player_colour = Column(String)
    turn_depth = Column(Integer)
    response_depth = Column(Integer)

    ### One to many relationships
    flashcards = relationship('Flashcard', backref = 'deck')

    def get_random_flashcard(self) -> Flashcard:
        return random.choice(self.flashcards)