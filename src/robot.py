from constants import (
    BOARD_SIZE_X,
    BOARD_SIZE_Y,
    VALID_X_RANGE,
    VALID_Y_RANGE,
    VALID_POSITIONS,
    ROTATION_MAP
)


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.position = None
    
    def _is_placed(self): 
        """
            Private fn to check that robot has been placed
        """
        return (
            self.x is not None and 
            self.y is not None and 
            self.position is not None
        )

    def place(self , x_cord, y_cord, position): 
        if type(x_cord) == str:
            x_cord = int(x_cord)
        if type(y_cord) == str:
            y_cord = int(y_cord)
        if not self._is_valid(x_cord, y_cord, position):
            # if robot hasnt been placed or placement  isnt valid, ignore cmd
            return 
    
        self.x = x_cord
        self.y = y_cord
        self.position = position

    def _is_valid(self, x_cord, y_cord, position):
        return (
            x_cord in VALID_X_RANGE and
            y_cord in VALID_Y_RANGE and 
            position in VALID_POSITIONS
        )
        
    def move(self):
        if not self._is_placed():
            return 

        curr_x = self.x
        curr_y = self.y 

        if self.position == 'NORTH': 
            curr_y += 1
        elif self.position == 'EAST': 
            curr_x += 1
        elif self.position == 'SOUTH':
            curr_y -= 1
        elif self.position == 'WEST': 
            curr_x -= 1
        
        if self._is_valid(curr_x, curr_y, self.position):
            # commit 
            self.x = curr_x
            self.y = curr_y

    def _rotate(self, direction):
        if not self._is_placed() or direction not in ['RIGHT', 'LEFT']:
            # invalid cmd if not placed or direction is not valid
            return 
        self.position = ROTATION_MAP[self.position][direction]


    def left(self): 
        self._rotate('LEFT')
    
    def right(self):
        self._rotate('RIGHT')
    
    def _grid_report(self): 
        """
            Code inspired from: https://stackoverflow.com/questions/60842728/developing-a-function-to-print-a-grid-in-python
        """
        print(f"\n  ", end='')
        for j in range(BOARD_SIZE_X):
            print(f"| {j} ", end='')
        print(f"| \n", end='')
        print(f'{(BOARD_SIZE_X*4+4)*"-"}')
        # Other rows
        for i in reversed(range(BOARD_SIZE_Y)):
            print(f"{i} ", end='')
            for j in range(BOARD_SIZE_X):
                if self.x == j and self.y == i:
                    print(f"| {self.position[0]} ", end='')
                else:
                    print(f"| . ", end='')
            print(f"| ", end='')
            print()
            print(f'{(BOARD_SIZE_X*4+4)*"-"}')

    def report(self):
        if not self._is_placed():
            # no report until robot is placed
            return None
        self._grid_report()
        print('\nX: {}, Y:{}, F:{}\n'.format(self.x, self.y, self.position))
        return [self.x, self.y, self.position]
        