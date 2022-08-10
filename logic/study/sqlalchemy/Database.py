
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session

from logic.consts.openings import openings
import logic.consts.filepaths as filepaths
from logic.study.sqlalchemy import Base
from logic.study.sqlalchemy.Deck import Deck
from logic.study.sqlalchemy.Flashcard import Flashcard
from logic.study.sqlalchemy.FlashcardMove import FlashcardMove
from logic.study.sqlalchemy.Opening import Opening
from logic.study.sqlalchemy.OpeningMove import OpeningMove # Not redundant - get weird "failed to locate a name" error without this

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
    
    def load_openings_from_static_file(self) -> None:
        for opening_dict in openings.values():
            if not self.session.query(Opening).filter_by(name = opening_dict['name']).count():
                opening = Opening(
                    name = opening_dict['name']
                )
                self.session.add(opening)
                self.session.commit()
                for move in opening_dict['moves']:
                    opening_move = OpeningMove(
                        opening_id = opening.id,
                        definition = move
                    )
                    self.session.add(opening_move)
                self.session.commit()

    def persist_deck(self, opening_id: int, player_color: str, turn_depth: int, response_depth: int) -> Deck:
        deck = Deck(
            opening_id = opening_id,
            player_color = player_color,
            turn_depth = turn_depth,
            response_depth = response_depth
        )
        self.session.add(deck)
        self.commit()
        return deck
    
    def persist_flashcard(self, deck_id: int, moves: List[str], best_move: str, algebraic_best_move: str, algebraic_opponents_move: str) -> Flashcard:
        flashcard = Flashcard(
            deck_id = deck_id,
            best_move = best_move,
            algebraic_best_move = algebraic_best_move,
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
    
    def delete_deck(self, deck: Deck) -> None:
        self.session.delete(deck)
        self.commit()
    
    def get_opening_by_name(self, opening_name: str) -> Opening:
        return self.session.query(Opening).filter_by(name = opening_name).first()

    def get_openings(self) -> List[Opening]:
        self.load_openings_from_static_file()
        return self.session.query(Opening).all()

def Database():
    global instance
    if instance is None:
        instance = _Database()
    return instance