from stockfish import Stockfish

import logic.consts.filepaths as filepaths
import logic.consts.deck_positions as deck_positions
from logic.enums.Color import Color
from logic.study.DeckGenerator import DeckGenerator

stockfish = Stockfish(filepaths.STOCKFISH)
deck_generator = DeckGenerator(
    deck_position_dict = deck_positions.ITALIAN_GAME,
    turn_depth = 2,
    response_depth = 2,
    player_color = Color.WHITE
)
num_flashcards = deck_generator.estimate_flashcard_number()
print(f'Generating up to {num_flashcards} flashcards...')
deck = deck_generator.generate(stockfish)

sorted_flashcards = sorted(deck.flashcards, key = lambda x: len(x.moves))
for i, flashcard in enumerate(sorted_flashcards, 1):
    print(str(i) + ': ' + str(flashcard.moves) + ' | ' + flashcard.your_best_move)