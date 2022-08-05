
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session

from logic.consts.start_positions import start_positions
from logic.consts.filepaths import DATABASE_URL
from logic.study.sqlalchemy import Base
from logic.study.sqlalchemy.Flashcard import Flashcard
from logic.study.sqlalchemy.Deck import Deck
from logic.study.sqlalchemy.StartPosition import StartPosition
from logic.study.sqlalchemy.StartPositionMove import StartPositionMove

instance = None

class _Database:
    database_filepath: str
    engine: Engine
    session: Session

    def __init__(self) -> None:
        self.database_url = DATABASE_URL
        self.engine = create_engine(self.database_url, echo = False)
        Base.metadata.create_all(self.engine, checkfirst = True)
        self.session = scoped_session(sessionmaker(bind = self.engine))
        self.load_start_positions_from_file()
    
    def commit(self) -> None:
        self.session.commit()
    
    def encode_moves(self, moves: List[str]) -> str:
        return '[{}]'.format(','.join(moves))
    
    def load_start_positions_from_file(self) -> List[StartPosition]:
        self.session.query(StartPosition).delete()
        self.session.query(StartPositionMove).delete()
        for start_position_dict in start_positions.values():
            start_position = StartPosition(name = start_position_dict['name'])
            self.session.add(start_position)
            self.commit()
            for move in start_position_dict['moves']:
                start_position_move = StartPositionMove(
                    start_position_id = start_position.id,
                    definition = move
                )
                self.session.add(start_position_move)
            self.commit()

    def persist_deck(self, start_position_id: int, player_colour: str, turn_depth: int, response_depth: int) -> Deck:
        deck = Deck(
            start_position_id = start_position_id,
            player_colour = player_colour,
            turn_depth = turn_depth,
            response_depth = response_depth
        )
        self.session.add(deck)
        return deck
    
    def persist_flashcard(self, deck_id: int, position: List[str], opponents_move: str, your_best_move: str) -> Flashcard:
        flashcard = Flashcard(
            deck_id = deck_id,
            position = position,
            opponents_move = opponents_move,
            your_best_move = your_best_move
        )
        self.session.add(flashcard)
        return flashcard

    def get_decks(self) -> List[Deck]:
        return self.session.query(Deck).all()
    
    def get_start_position(self, name: str) -> StartPosition:
        return (self.session.query(StartPosition)
                            .filter_by(name = name)
                            .first())

def Database():
    global instance
    if instance is None:
        instance = _Database()
    return instance