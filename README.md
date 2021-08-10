# toyrob
<h2>Prerequisites</h2>

- Python3 with pip
- Make 3.8 + 

<h2>Description and requirements:</h2>
The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.
Create a console application that can read in commands of the following form -

```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0)
can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE
command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The
application should discard all commands in the sequence until a valid PLACE command has been executed.
MOVE will move the toy robot one unit forward in the direction it is currently facing.
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.
A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.
Input can be from a file, or from standard input, as the developer chooses.
Provide test data to exercise the application.
It is not required to provide any graphical output showing the movement of the toy robot.
The application should handle error states appropriately and be robust to user input.
Constraints:
The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any
move that would cause the robot to fall must be ignored.

<h2>Setup</h2>

1. Build virtual python environment: 

```
make vp
```

2. Running application locally: <br>
  a. To run app using stdin run: `make run_py` <br/>
  b. To run app using a file for commands:
  ```
  make run_py CMDLIST_FILE=$FILE_PATH
  e.g 
  make run_py CMDLIST_FILE=test_list
  ```
4. Running tests: `make test`
   - This will generate a coverage report in `./output/coverage`. Opening `./output/coverage/index.html` will give a breakdown of the report
6. clean up: deleting virtual python and coverage reports -> `make clean` 
