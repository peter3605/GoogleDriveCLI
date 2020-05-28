def display():
    f = open('welcome.txt', 'r')
    for i in range(0,6):
        line = f.readline().strip()
        if i == 0 or i == 5:
            line = " " + line
        print(line)

    print(' --------------------------')
    print('| TO THE GOOGLE DRIVE CLI! |')
    print(' --------------------------')