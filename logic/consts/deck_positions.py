ITALIAN_GAME = {
    'name': 'Italian Game',
    'moves': ['e2e4','e7e5','g1f3','b8c6','f1c4']
}

RUY_LOPEZ_OPENING = {
    'name': 'Ruy Lopez Opening',
    'moves': ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5']
}

CENTER_GAME_ACCEPTED_QXD4 = {
    'name': 'Center Game Accepted: 3.Qxd4',
    'moves': ['e2e4', 'e7e5', 'd2d4', 'e5d4', 'd1d4']
}

SICILIAN_DEFENCE = {
    'name': 'Sicilian Defence',
    'moves': ['e2e4', 'c7c5']
}

# CAPTURE_TEST = {
#     'name': 'Capture Test',
#     'moves': ['e2e4', 'd7d5', 'e4d5']
# }

deck_positions = {k: v for k, v in locals().items() if not k.startswith('__')}