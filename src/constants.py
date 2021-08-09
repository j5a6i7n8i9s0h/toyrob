BOARD_SIZE = 5 

BOARD_SIZE_X = BOARD_SIZE # can be adjusted to handle different sized grids
BOARD_SIZE_Y = BOARD_SIZE

VALID_X_RANGE = set(range(BOARD_SIZE_X))
VALID_Y_RANGE = set(range(BOARD_SIZE_Y))

VALID_POSITIONS = {
    'NORTH',
    'EAST',
    'SOUTH',
    'WEST'
}

# rotation map to handle logic for turning in appropriate direction
ROTATION_MAP = {
    'NORTH': {
        'RIGHT': 'EAST',
        'LEFT': 'WEST'
    },
    'EAST': {
        'RIGHT': 'SOUTH',
        'LEFT': 'NORTH'
    },
    'SOUTH': {
        'RIGHT': 'WEST',
        'LEFT': 'EAST'
    },
    'WEST': {
        'RIGHT': 'NORTH',
        'LEFT': 'SOUTH'
    }
}

VALID_CMDS = [
    'PLACE',
    'MOVE',
    'LEFT',
    'RIGHT',
    'REPORT'
]