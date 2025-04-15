'''
Ben Frederick
CS 1210
'''

def code_stats(filename):
    total = 0
    lines_long = 0
    avg_len = 0
    x = 0
    with open(filename, 'r') as file:
        for line in file:
            if line != '':
                total += 1
            if len(line) > 40:
                lines_long += 1
            x += 1
        avg_len = (total + lines_long) / x
        print(f'{filename} stats')
        print(f'total lines: {total}')
        print(f'long lines: {lines_long}')
        print(f'average length: {avg_len}')


def line_numbers(filename):
    x = 1
    with open(filename, 'r') as file:
        for line in file:
            if x < 10:
                if len(line) > 40:
                    print(f'\033[1m {x}: {line}\033[0m', end='')
                    x += 1
                else:
                    print(f' {x}: {line}', end='')
                    x += 1
            else:
                if len(line) > 40:
                    print(f'\033[1m {x}: {line}\033[0m', end='')
                    x += 1
                else:
                    print(f' {x}: {line}', end='')
                    x += 1
if __name__ == '__main__':
    code_stats('lab_10.py')
    line_numbers('lab_10.py')