from sqlalchemy import Column, ForeignKey, Integer, String

from logic.study.sqlalchemy import Base

class DeckMove(Base):
    __tablename__ = 'deck_move'

    id = Column(Integer, primary_key = True, autoincrement = True)
    deck_id = Column(Integer, ForeignKey('deck.id'))
    definition = Column(String)

    def from_square(self) -> str:
        return self.definition[:2]
    
    def to_square(self) -> str:
        return self.definition[2:]