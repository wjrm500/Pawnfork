from stockfish import Stockfish

stockfish = Stockfish(path = "stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")

moves = {}
for i in stockfish.get_top_moves(3):
    stockfish.set_position([i['Move']])
    moves[i['Move']] = [j for j in stockfish.get_top_moves(3)]


ITALIAN_GAME = ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4']

class Flashcard:
    sf = stockfish

    def __init__(self, position, best_move) -> None:
        self.position = position
        self.opponents_move = position[-1] if len(position) > 0 else ''
        self.your_best_move = best_move

    def __str__(self) -> str:
        Flashcard.sf.set_position(self.position)
        return Flashcard.sf.get_board_visual() + '\n' + 'Opponent did: ' + self.opponents_move + '\n' + 'Your best move is: ' + self.your_best_move + '\n\n'

flashcards = []
def get_best_moves(start_position, turn_depth, response_depth):
    white_to_move = len(start_position) % 2 == 0
    stockfish.set_position(start_position)
    if turn_depth == 0:
        return
    else:
        temp_response_depth = 1 if white_to_move else response_depth
        for response in stockfish.get_top_moves(temp_response_depth):
            if white_to_move:
                flashcard = Flashcard(start_position, response['Move'])
                flashcards.append(flashcard)
                turn_depth -= 1
            new_position = start_position + [response['Move']]
            get_best_moves(new_position, turn_depth, response_depth)

td = 10
rd = 3
num_flashcards = sum([rd ** n for n in range(td)])
print(f'Generating {num_flashcards} flashcards...')
get_best_moves([], td, rd)
# get_best_moves(ITALIAN_GAME, 5, 3)
sorted_flashcards = sorted(flashcards, key = lambda x: len(x.position))
for i, flashcard in enumerate(sorted_flashcards, 1):
    print(str(i) + ': ' + str(flashcard.position) + ' | ' + flashcard.your_best_move)