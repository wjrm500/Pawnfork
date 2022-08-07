
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session

from logic.consts.deck_positions import deck_positions
import logic.consts.filepaths as filepaths
from logic.study.sqlalchemy import Base
from logic.study.sqlalchemy.Flashcard import Flashcard
from logic.study.sqlalchemy.Deck import Deck
from logic.study.sqlalchemy.DeckPosition import DeckPosition
from logic.study.sqlalchemy.DeckPositionMove import DeckPositionMove

instance = None

class _Database:
    database_filepath: str
    engine: Engine
    session: Session

    def __init__(self) -> None:
        self.database_url = filepaths.DATABASE
        self.engine = create_engine(self.database_url, echo = False)
        Base.metadata.create_all(self.engine, checkfirst = True)
        self.session = scoped_session(sessionmaker(bind = self.engine))
        self.load_deck_positions_from_file()
    
    def commit(self) -> None:
        self.session.commit()
    
    def encode_moves(self, moves: List[str]) -> str:
        return '[{}]'.format(','.join(moves))
    
    def load_deck_positions_from_file(self) -> List[DeckPosition]:
        self.session.query(DeckPosition).delete()
        self.session.query(DeckPositionMove).delete()
        for deck_position_dict in deck_positions.values():
            deck_position = DeckPosition(name = deck_position_dict['name'])
            self.session.add(deck_position)
            self.commit()
            for move in deck_position_dict['moves']:
                deck_position_move = DeckPositionMove(
                    deck_position_id = deck_position.id,
                    definition = move
                )
                self.session.add(deck_position_move)
            self.commit()

    def persist_deck(self, deck_position_id: int, player_colour: str, turn_depth: int, response_depth: int) -> Deck:
        deck = Deck(
            deck_position_id = deck_position_id,
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
    
    def get_deck_position(self, name: str) -> DeckPosition:
        return (self.session.query(DeckPosition)
                            .filter_by(name = name)
                            .first())

def Database():
    global instance
    if instance is None:
        instance = _Database()
    return instance