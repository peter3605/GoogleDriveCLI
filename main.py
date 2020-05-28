from drive_commands import DriveObj
import error_messages as error
import welcome_message as welcome

options = ["login","exit", "print"]

# represents a connection to google drive
drive = None
logged_in = False

"""
Parse the command
"""
def parse_command(command):
    # split the command by whitespace
    split = command.split()

    # if the string was empty or too small, print invalid command and return none
    if split is None or len(split) < 1 or split[0] is None:
        error.print_invalid_command()
        return None
    
    # get the main command - should be the first word
    args = {'main':split[0]}

    # need to parse for flags and other stuff

    return args

"""
Validate and run the command
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
    elif main_command == 'login' and size == 1:
        try:
            drive.login()
            logged_in = True
        except:
            error.print_login_error()
    elif main_command == 'print' and size == 1:
        if logged_in:
            drive.print_n_filenames()
        else:
            error.print_not_logged_in_error()
    else:
        error.print_invalid_command()

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


if __name__ == '__main__':
    main()