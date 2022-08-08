
from typing import Dict, List
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session

import logic.consts.filepaths as filepaths
from logic.study.sqlalchemy import Base
from logic.study.sqlalchemy.Flashcard import Flashcard
from logic.study.sqlalchemy.Deck import Deck
from logic.study.sqlalchemy.DeckMove import DeckMove
from logic.study.sqlalchemy.FlashcardMove import FlashcardMove

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
    
    def commit(self) -> None:
        self.session.commit()
    
    def encode_moves(self, moves: List[str]) -> str:
        return '[{}]'.format(','.join(moves))

    def persist_deck(self, deck_position_dict: Dict, player_color: str, turn_depth: int, response_depth: int) -> Deck:
        deck = Deck(
            name = deck_position_dict['name'],
            player_color = player_color,
            turn_depth = turn_depth,
            response_depth = response_depth
        )
        self.session.add(deck)
        self.commit()
        for move in deck_position_dict['moves']:
            deck_move = DeckMove(
                deck_id = deck.id,
                definition = move
            )
            self.session.add(deck_move)
        return deck
    
    def persist_flashcard(self, deck_id: int, moves: List[str], your_best_move: str, algebraic_opponents_move: str) -> Flashcard:
        flashcard = Flashcard(
            deck_id = deck_id,
            your_best_move = your_best_move,
            algebraic_opponents_move = algebraic_opponents_move
        )
        self.session.add(flashcard)
        self.commit()
        for move in moves:
            flashcard_move = FlashcardMove(
                flashcard_id = flashcard.id,
                definition = move
            )
            self.session.add(flashcard_move)
        return flashcard

    def get_decks(self) -> List[Deck]:
        return self.session.query(Deck).all()

def Database():
    global instance
    if instance is None:
        instance = _Database()
    return instance