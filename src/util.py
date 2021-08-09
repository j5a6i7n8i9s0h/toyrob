
from constants import VALID_CMDS

def parse_line(line): 
    command_list = line.split()
    print(command_list)
    if command_list[0] not in VALID_CMDS:
        return 
    cmd = command_list[0].lower()
    arg_list = []
    if command_list[0] == 'PLACE': 
        if len(command_list) !=2 or len(command_list[1].split(',')) !=3:  
            return 
        arg_list = command_list[1].split(',')
    return cmd, arg_list

def parse_file(file_, robot):
    for line in file_: 
        cmd, extra_args = parse_line(line)
        if cmd == 'place': 
            robot.place(*extra_args)
        else: 
            if hasattr(robot, cmd) and callable(getattr(robot, cmd)):
                getattr(robot, cmd)()
        
        

