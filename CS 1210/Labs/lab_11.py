'''
Ben Frederick
CS 1210
'''
import matplotlib.pyplot as plt
import random


def survey():
    b = random.randint(1 , 365)
    c = []
    x = 0
    z = 0
    while z == 0:
        b = random.randint(1 , 365)
        if b in c:
            z += 1 
        else:
            c.append(b)
            x += 1
    return x


def birthday_odds(n):
    l = []
    q = 0
    for i in range(n):
        l.append(random.randint(1 , 365))
    l.sort()
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            q += 1
    if q:
        return True
    else:
        return False
    
if __name__ == '__main__':
    #Excerise 1
    vals_hist = []
    for i in range(1000):
        vals_hist.append(survey())
    plt.hist(vals_hist)
    plt.title('UVM students surveyed to find matching birthdays')
    plt.xlabel('Students Surveyed')
    plt.ylabel('Frequency')
    plt.show()

    #Excercise 2
    datay = []
    c = 0
    for i in range(70):
        c = 0
        for f in range(100):
            if birthday_odds(i):
                c += 1
        datay.append(c / 100)
    datax = []
    for i in range(1 , 71):
        datax.append(i)
    plt.plot(datax, datay)
    plt.title('Probability of matching birthdays in n class size')
    plt.xlabel('Class size (n)')
    plt.ylabel('Probability of matching birthday in class')
    plt.show()