# from stockfish import Stockfish

# from logic.consts.filepaths import STOCKFISH_FILEPATH

class Flashcard:
    # stockfish = Stockfish(STOCKFISH_FILEPATH)

    def __init__(self, position, best_move) -> None:
        self.position = position
        self.opponents_move = position[-1] if len(position) > 0 else ''
        self.your_best_move = best_move

    # def __str__(self) -> str:
    #     Flashcard.stockfish.set_position(self.position)
    #     return Flashcard.stockfish.get_board_visual() + '\n' + 'Opponent did: ' + self.opponents_move + '\n' + 'Your best move is: ' + self.your_best_move + '\n\n'