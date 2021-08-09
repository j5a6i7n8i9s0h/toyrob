import fileinput, argparse

from robot import Robot
from util import parse_line, parse_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cmdlist', help="File path containing commands for toy robot", default="-") # defaults to stdin
    arguments = parser.parse_args()
    robot_obj = Robot()
    file_input_args = {}
    if arguments.cmdlist != '-': 
        file_input_args['files'] = (arguments.cmdlist)

    with fileinput.input(**file_input_args) as f: 
        parse_file(f, robot_obj)


