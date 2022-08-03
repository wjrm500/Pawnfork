from stockfish import Stockfish

import logic.consts.colours as colours
from logic.consts.filepaths import STOCKFISH_FILEPATH
import logic.consts.positions as positions
from logic.study.FlashcardGenerator import FlashcardGenerator

stockfish = Stockfish(STOCKFISH_FILEPATH)
flashcard_generator = FlashcardGenerator(
    start_position = positions.ITALIAN_GAME,
    turn_depth = 2,
    response_depth = 2,
    player_colour = colours.WHITE
)
num_flashcards = flashcard_generator.estimate_flashcard_number()
print(f'Generating up to {num_flashcards} flashcards...')
flashcards = flashcard_generator.generate(stockfish)
sorted_flashcards = sorted(flashcards, key = lambda x: len(x.position))
for i, flashcard in enumerate(sorted_flashcards, 1):
    print(str(i) + ': ' + str(flashcard.position) + ' | ' + flashcard.your_best_move)