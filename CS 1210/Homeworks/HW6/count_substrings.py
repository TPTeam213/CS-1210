''''
Ben Frederick 
CS 1210
'''

#Never thought slicing would be useful :|
def substring_count(stg , sub):
    x = 0
    z = 0
    if sub != '':
        for i in range(len(stg)):
            if stg[i:len(sub) + z] == sub:
                x += 1
            z += 1
        return x
    else:
        return 0

if __name__ == '__main__':
    stg = input('Enter a string: ')
    sub = input('Enter a substring: ')
    print(substring_count(stg,sub))