from sqlalchemy import Column, ForeignKey, Integer, String

from logic.study.sqlalchemy import Base

class OpeningMove(Base):
    __tablename__ = 'opening_move'

    id = Column(Integer, primary_key = True, autoincrement = True)
    opening_id = Column(Integer, ForeignKey('opening.id'))
    definition = Column(String)

    def from_square(self) -> str:
        return self.definition[:2]
    
    def to_square(self) -> str:
        return self.definition[2:]