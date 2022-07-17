from stockfish import Stockfish

stockfish = Stockfish(path = "stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")

for i in stockfish.get_top_moves(5):
    print(i)