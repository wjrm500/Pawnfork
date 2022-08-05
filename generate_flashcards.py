from stockfish import Stockfish

from logic.consts.filepaths import STOCKFISH_FILEPATH
import logic.consts.positions as positions
from logic.enums.Colour import Colour
from logic.study.DeckGenerator import DeckGenerator

stockfish = Stockfish(STOCKFISH_FILEPATH)
deck_generator = DeckGenerator(
    start_position = positions.ITALIAN_GAME,
    turn_depth = 2,
    response_depth = 2,
    player_colour = Colour.WHITE
)
num_flashcards = deck_generator.estimate_flashcard_number()
print(f'Generating up to {num_flashcards} flashcards...')
deck = deck_generator.generate(stockfish)

sorted_flashcards = sorted(deck.flashcards, key = lambda x: len(x.position))
for i, flashcard in enumerate(sorted_flashcards, 1):
    print(str(i) + ': ' + str(flashcard.position) + ' | ' + flashcard.your_best_move)