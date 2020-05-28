def display():
    f = open('welcome.txt', 'r')
    for i in range(0,22):
        line = f.readline().rstrip()
        print(line)

    print('              -------------------------------------------')
    print('              | COMMAND LINE INTERFACE FOR GOOGLE DRIVE |')
    print('              -------------------------------------------')