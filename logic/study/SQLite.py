import sqlite3

from logic.consts.filepaths import SQLITE_FILEPATH
from logic.study.Deck import Deck

class SQLite:
    def __init__(self) -> None:
        self.connect()
    
    def connect(self) -> None:
        self.conn = sqlite3.connect(SQLITE_FILEPATH)
        self.cursor = self.conn.cursor()
    
    def create_deck_table_if_not_exists(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS deck (
                id INTEGER PRIMARY KEY,
                start_position TEXT,
                player_colour TEXT
            )
        """
        self.cursor.execute(sql)
        self.conn.commit()
    
    def create_flashcard_table_if_not_exists(self) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS flashcard (
                id INTEGER PRIMARY KEY,
                deck_id INTEGER,
                position TEXT,
                opponents_move TEXT,
                your_best_move TEXT
            )
        """
        self.cursor.execute(sql)
        self.conn.commit()
    
    def persist_deck(self, deck: Deck) -> None:
        # Insert deck
        self.create_deck_table_if_not_exists()
        deck_insert_sql = 'INSERT INTO deck (start_position, player_colour) VALUES (?, ?)'
        self.cursor.execute(
            deck_insert_sql,
            (
                '[' + ','.join(deck.start_position) + ']',
                deck.player_colour.value
            )
        )
        deck_id = self.cursor.lastrowid
        
        # Insert flashcards
        self.create_flashcard_table_if_not_exists()
        flashcard_insert_sql = 'INSERT INTO flashcard (deck_id, position, opponents_move, your_best_move) VALUES (?, ?, ?, ?)'
        for flashcard in deck:
            self.cursor.execute(
                flashcard_insert_sql,
                (
                    deck_id,
                    '[' + ','.join(flashcard.position) + ']',
                    flashcard.opponents_move,
                    flashcard.your_best_move
                )
            )
        
        self.conn.commit()