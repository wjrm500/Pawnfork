from sqlalchemy import Column, ForeignKey, Integer, String

from logic.study.sqlalchemy import Base

class StartPositionMove(Base):
    __tablename__ = 'start_position_move'

    id = Column(Integer, primary_key = True, autoincrement = True)
    start_position_id = Column(Integer, ForeignKey('start_position.id'))
    definition = Column(String)

    def from_square(self) -> str:
        return self.definition[:2]
    
    def to_square(self) -> str:
        return self.definition[2:]