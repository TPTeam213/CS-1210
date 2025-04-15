'''
Ben Frederick
CS 1210
'''

def mean(x):
    return sum(x) / len(x)


def std_dev(x):
    keep = []
    for i in range(len(x)):
        keep.append( (x[i] - mean(x)) ** 2 )
    return (sum(keep) / len(x)) ** .5


if __name__ == '__main__':
    y = 0
    data = []
    while y == 0:
        inp = input('Enter a real number or q to end data entry: ')
        if inp != 'q':
            data.append(float(inp))
        else:
            y += 1
            if len(data) == 0:
                print('No data!')
            else:
                print(f'The mean is {mean(data):.2f} '
                      f'and the standard deviation is {std_dev(data):.2f}')