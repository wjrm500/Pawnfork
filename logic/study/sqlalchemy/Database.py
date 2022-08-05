
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session

from logic.consts.filepaths import DATABASE_URL
from logic.study.sqlalchemy import Base
from logic.study.sqlalchemy.Flashcard import Flashcard
from logic.study.sqlalchemy.Deck import Deck

class Database:
    database_filepath: str
    engine: Engine
    session: Session

    def __init__(self) -> None:
        self.database_url = DATABASE_URL
        self.engine = create_engine(self.database_url, echo = False)
        Base.metadata.create_all(self.engine, checkfirst = True)
        self.session = scoped_session(sessionmaker(bind = self.engine))
    
    def commit(self) -> None:
        self.session.commit()

    def persist_deck(self, start_position: str, player_colour: str) -> Deck:
        deck = Deck(
            start_position = start_position,
            player_colour = player_colour
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