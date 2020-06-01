from drive import DriveObj
import error_messages as error
import welcome_message as welcome
import commands
import re

# represents a connection to google drive
drive = None
logged_in = False

"""
Parses the user input - splits into the main command and the flags/arguments
    Params: command - passed from the main method, contains the raw input string from command line
    Returns: result - a dictionary containing the command and arguments
"""
def parse_command(command):
    # what is returned
    result = {}

    # regex strings
    input_pattern = '^([a-z]+)( -[a-z]* \S*)*$'
    main_pattern = '^([a-z]+)'
    args_pattern = '( -[a-z]* \S*)'

    # check the command for regex match
    match = re.search(input_pattern, command)

    # if it does not match, return None
    if match is None:
        result = None
    else:
        # otherwise, find the groups
        main = re.search(main_pattern, command).group(0)
        args = [x.group() for x in re.finditer(args_pattern, command)]

        # add the main command to dictionary
        result['main'] = main
        
        # split the args and put into result
        for arg in args:
            split = arg.split()
            result[split[0]] = split[1]

    return result

"""
Validate and run the command - checks if the main command is a valid one
    Params: args - the dictionary of commands/arguments from the parse_command method
    Returns: nothing
"""
def run_command(args):
    # variables that will be used
    main_command = args['main']
    size = len(args)
    global drive
    global logged_in

    # check the main command
    if main_command == 'exit':
        exit()
    elif main_command == 'login' and check_size(args, 1):
        try:
            drive.login()
            logged_in = True
        except:
            error.print_login_error()
    elif main_command == 'filenames' and check_size(args, 1, 2):
        if logged_in:
            drive.view_filenames(args)
        else:
            error.print_not_logged_in_error()
    elif main_command == 'foldernames' and check_size(args, 1, 2):
        if logged_in:
            drive.view_foldernames()
        else:
            error.print_not_logged_in_error()
    elif main_command == "help" and check_size(args, 1):
        commands.print_commands()
    else:
        error.print_invalid_command()

"""
Checks the size of args
"""
def check_size(args, *nums):
    for num in nums:
        if len(args) == num:
            return True
    return False

"""
Start the CLI
"""
def main():
    # print the welcome message
    welcome.display()

    # create a drive object
    global drive 
    drive = DriveObj()

    # read commands
    while True:
        command = input('% ')
        args = parse_command(command)
        if args is not None:
            run_command(args)
        else:
            error.print_invalid_command()


if __name__ == '__main__':
    main()