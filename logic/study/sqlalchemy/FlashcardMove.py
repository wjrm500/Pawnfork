from sqlalchemy import Column, ForeignKey, Integer, String

from logic.study.sqlalchemy import Base

class FlashcardMove(Base):
    __tablename__ = 'flashcard_move'

    id = Column(Integer, primary_key = True, autoincrement = True)
    flashcard_id = Column(Integer, ForeignKey('flashcard.id'))
    definition = Column(String)
    algebraic_definition = Column(String)

    def from_square(self) -> str:
        return self.definition[:2]
    
    def to_square(self) -> str:
        return self.definition[2:]