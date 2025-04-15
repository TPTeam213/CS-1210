'''
Ben Frederick
CS 1210
'''

if __name__ == '__main__':
    while True:
        z = 0
        fname = input('Enter the file name: ')
        fname = fname.lower()
        if fname == 'q':
            break
        try:
            with open(fname, 'r') as file:
                print()
        except FileNotFoundError:
            print('File not found!')
            z = 1
        if z == 0:
            with open(fname, 'r') as file:
                for line in file:
                    print(str(line))
            break