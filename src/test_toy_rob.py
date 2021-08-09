from util import parse_file
from robot import Robot

class TestLixi:
    def test_invalid_type(self):
        # setup
        robot_obj = Robot()

        # execute

        # verify
        parse_file(
            "PLACE 1,2,EAST\nMOVE\nMOVE\nLEFT\nMOVE\nMOVE\nREPORT",
            robot_obj
        )