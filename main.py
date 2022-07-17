from stockfish import Stockfish

fish = Stockfish(path = "stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")

class Colour:
    WHITE = 'white'
    BLACK = 'black'

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
def generate_flashcards(start_position, turn_depth, response_depth, player_colour = Colour.WHITE):
    if turn_depth == 0:
        return
    colour_to_move = Colour.WHITE if len(start_position) % 2 == 0 else Colour.BLACK
    player_to_move = colour_to_move == player_colour
    fish.set_position(start_position)
    if player_to_move:
        top_moves = fish.get_top_moves(1)
        top_move = top_moves[0]
        flashcard = Flashcard(start_position, top_move['Move'])
        flashcards.append(flashcard)
        turn_depth -= 1
        new_position = start_position + [top_move['Move']]
        generate_flashcards(new_position, turn_depth, response_depth, player_colour)
    else: # Opponent to move
        top_moves = fish.get_top_moves(response_depth)
        centipawns = [x['Centipawn'] for x in top_moves]
        best_centipawn = min(centipawns) if player_colour == Colour.WHITE else max(centipawns) # i.e. Centipawn value of opponent's best move
        filter_good_moves = lambda x: x['Centipawn'] < best_centipawn + 100 if player_colour == Colour.WHITE else lambda x: x['Centipawn'] > best_centipawn - 100
        good_top_moves = filter(filter_good_moves, top_moves) # Filter out any opponent moves that are significantly worse than the best move
        for top_move in good_top_moves:
            new_position = start_position + [top_move['Move']]
            generate_flashcards(new_position, turn_depth, response_depth, player_colour)

position = ITALIAN_GAME
turn_depth = 3
response_depth = 3
player_colour = Colour.WHITE
num_flashcards = sum([response_depth ** n for n in range(turn_depth)])
colour_to_move = Colour.WHITE if len(position) % 2 == 0 else Colour.BLACK
player_to_move = colour_to_move == player_colour
num_flashcards = num_flashcards if player_to_move else num_flashcards * response_depth
print(f'Generating up to {num_flashcards} flashcards...')
generate_flashcards(position, turn_depth, response_depth, player_colour)
sorted_flashcards = sorted(flashcards, key = lambda x: len(x.position))
for i, flashcard in enumerate(sorted_flashcards, 1):
    print(str(i) + ': ' + str(flashcard.position) + ' | ' + flashcard.your_best_move)