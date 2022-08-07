ITALIAN_GAME = {
    'name': 'Italian Game',
    'moves': ['e2e4','e7e5','g1f3','b8c6','f1c4']
}

RUY_LOPEZ_OPENING = {
    'name': 'Ruy Lopez Opening',
    'moves': ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5']
}

deck_positions = {k: v for k, v in locals().items() if not k.startswith('__')}