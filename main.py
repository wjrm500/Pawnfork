from stockfish import Stockfish

fish = Stockfish(path = "stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")

moves = {}
for i in fish.get_top_moves(3):
    fish.set_position([i['Move']])
    moves[i['Move']] = [j for j in fish.get_top_moves(3)]


ITALIAN_GAME = ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4']

class Flashcard:
    sf = fish

    def __init__(self, position, best_move) -> None:
        self.position = position
        self.opponents_move = position[-1] if len(position) > 0 else ''
        self.your_best_move = best_move

    def __str__(self) -> str:
        Flashcard.sf.set_position(self.position)
        return Flashcard.sf.get_board_visual() + '\n' + 'Opponent did: ' + self.opponents_move + '\n' + 'Your best move is: ' + self.your_best_move + '\n\n'

flashcards = []
def generate_flashcards(start_position, turn_depth, response_depth):
    if turn_depth == 0:
        return
    white_to_move = len(start_position) % 2 == 0
    fish.set_position(start_position)
    if white_to_move:
        top_moves = fish.get_top_moves(1)
        top_move = top_moves[0]
        flashcard = Flashcard(start_position, top_move['Move'])
        flashcards.append(flashcard)
        turn_depth -= 1
        new_position = start_position + [top_move['Move']]
        generate_flashcards(new_position, turn_depth, response_depth)
    else: # Black to move
        top_moves = fish.get_top_moves(response_depth)
        min_centipawn = min([x['Centipawn'] for x in top_moves]) # i.e. Centipawn value of black's best move
        good_top_moves = [x for x in top_moves if x['Centipawn'] < min_centipawn + 100] # Filter out any black moves that are significantly worse than the best move
        for top_move in good_top_moves:
            new_position = start_position + [top_move['Move']]
            generate_flashcards(new_position, turn_depth, response_depth)

position = ITALIAN_GAME
td = 3
rd = 2
num_flashcards = sum([rd ** n for n in range(td)])
print(f'Generating up to {num_flashcards} flashcards...')
generate_flashcards([], td, rd)
sorted_flashcards = sorted(flashcards, key = lambda x: len(x.position))
for i, flashcard in enumerate(sorted_flashcards, 1):
    print(str(i) + ': ' + str(flashcard.position) + ' | ' + flashcard.your_best_move)