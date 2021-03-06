commands = ['login', 'exit', 'filenames', 'foldernames', 'cd', 'help']

command_descriptions = {
    'login':'If you have not logged in before using the drive CLI, this command takes you to the Google Drive login screen. Note that you must have enabled the Drive API option on your account and must have the credentials.json file downloaded.' ,
    'exit':'Used to exit the Drive CLI',
    'filenames':'View the n most recently updated files in your drive\n   [-n] --> specifies how many file names you want(default is 10\n   Example: file-names -n 5',
    'foldernames':'View the folders in the current directory',
    'cd':'Change directory into the specified folder\n [-f] --> Specifies folder(default is root folder)',
    'help':'Displays the possible commands'
}

def print_commands():
    print('Possible commands:')
    for command in commands:
        print(f'{command} - {command_descriptions[command]}\n')