from typing import Literal

ITALIAN_GAME = ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4']

positions = [v for k, v in locals().items() if not k.startswith('__')]
Position = Literal[tuple(positions)]