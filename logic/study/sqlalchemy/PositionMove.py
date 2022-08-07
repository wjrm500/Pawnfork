from sqlalchemy import Column, ForeignKey, Integer, String

from logic.study.sqlalchemy import Base

class PositionMove(Base):
    __tablename__ = 'deck_position_move'

    id = Column(Integer, primary_key = True, autoincrement = True)
    position_id = Column(Integer, ForeignKey('position.id'))
    definition = Column(String)

    def from_square(self) -> str:
        return self.definition[:2]
    
    def to_square(self) -> str:
        return self.definition[2:]