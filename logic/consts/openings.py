CARO_KANN_DEFENCE = {
    'name': 'Caro-Kann Defence',
    'moves': ['e2e4', 'c7c6']
}

CENTER_GAME = {
    'name': 'Center Game',
    'moves': ['e2e4', 'e7e5', 'd2d4', 'e5d4']
}

ENGLISH_OPENING = {
    'name': 'English Opening',
    'moves': ['c2c4']
}

FRENCH_DEFENCE = {
    'name': 'French Defence',
    'moves': ['e2e4', 'e7e6']
}

KINGS_GAMBIT = {
    'name': 'King\'s Gambit',
    'moves': ['e2e4', 'e7e5', 'f2f4']
}

KINGS_PAWN_OPENING = {
    'name': 'King\'s Pawn Opening',
    'moves': ['e2e4', 'e7e5']
}

ITALIAN_GAME = {
    'name': 'Italian Game',
    'moves': ['e2e4','e7e5','g1f3','b8c6','f1c4']
}

PIRC_DEFENCE = {
    'name': 'Pirc Defence',
    'moves': ['e2e4', 'd7d6']
}

QUEENS_GAMBIT = {
    'name': 'Queen\'s Gambit',
    'moves': ['d2d4', 'd7d5', 'c2c4']
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