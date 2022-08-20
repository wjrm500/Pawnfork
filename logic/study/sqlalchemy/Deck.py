import random
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from logic.study.sqlalchemy.Flashcard import Flashcard
from logic.study.sqlalchemy import Base

class Deck(Base):
    __tablename__ = 'deck'

    id = Column(Integer, primary_key = True, autoincrement = True)
    opening_id = Column(Integer, ForeignKey('opening.id'))
    player_color = Column(String)
    turn_depth = Column(Integer)
    response_depth = Column(Integer)

    ### One to many relationships
    flashcards = relationship('Flashcard', backref = 'deck', cascade = 'all,delete')

    used_flashcards = []

    def get_random_flashcard(self) -> Flashcard:
        random_flashcard = self.flashcards.pop(random.randrange(len(self.flashcards)))
        self.used_flashcards.append(random_flashcard)
        if len(self.flashcards) == 0:
            self.flashcards = self.used_flashcards.copy()
            self.used_flashcards = []
        return random_flashcard