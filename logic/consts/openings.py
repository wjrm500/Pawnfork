CENTER_GAME_ACCEPTED_QXD4 = {
    'name': 'Center Game Accepted: 3.Qxd4',
    'moves': ['e2e4', 'e7e5', 'd2d4', 'e5d4', 'd1d4']
}

KINGS_PAWN_OPENING = {
    'name': 'King\'s Pawn Opening',
    'moves': ['e2e4', 'e7e5']
}

ITALIAN_GAME = {
    'name': 'Italian Game',
    'moves': ['e2e4','e7e5','g1f3','b8c6','f1c4']
}

QUEENS_PAWN_OPENING = {
    'name': 'Queen\'s Pawn Opening',
    'moves': ['d2d4', 'd7d5']
}

RUY_LOPEZ_OPENING = {
    'name': 'Ruy Lopez Opening',
    'moves': ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5']
}

SICILIAN_DEFENCE = {
    'name': 'Sicilian Defence',
    'moves': ['e2e4', 'c7c5']
}

openings = {k: v for k, v in locals().items() if not k.startswith('__')}