from logic.board.Board import Board
from logic.board.Square import Square
from logic.study.sqlalchemy.Database import Database
from ui.Window import Window

# board = Board()

# ITALIAN_GAME = ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4']
# for move in ITALIAN_GAME:
#     from_square_str, to_square_str = move[:2], move[2:]
#     board.get_square(from_square_str).piece.move(board.get_square(to_square_str))

database = Database()
window = Window(database)
# window.main_frame.frame.canvas.add_pieces(board.pieces)
window.run()