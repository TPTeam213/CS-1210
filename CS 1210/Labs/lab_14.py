'''
Ben Frederick
CS 1210
'''
import random
import matplotlib.pyplot as plt

def erdos_renyi(n, p):
    things = []
    graph = {}
    for i in range(n):
        graph[i] = []
    for u in graph:
        for v in graph:
            if u < v:
                things.append([u,v])
    for combo in things:
        r = random.random()
        if r < p:
            graph[combo[0]].append(combo[1])
            graph[combo[1]].append(combo[0])
    return graph


def barabasi_albert(n):
    graph = {0: [1], 1: [0]}
    edges = [(0, 1)]
    for i in range(2, n):
        x1 = random.choice(edges)
        y1 = random.choice(x1)
        x2 = random.choice(edges)
        y2 = random.choice(x2)
        while y2 == y1:
            x2 = random.choice(edges)
            y2 = random.choice(x2)
        edges.append((i,y2))
        graph[i] = [y1, y2]
        graph[y1].append(i)
        graph[y2].append(i)
    return graph


def max_degree(graph):
    hold = 0
    for val in graph.values():
        if len(val) > hold:
            hold = len(val)
    return hold


if __name__ == '__main__':
    avg_maxs1 = []
    avg_maxs2 = []
    for i in range(1,100):
        maxs1 = []
        maxs2 = []
        for z in range(100):
            maxs1.append(max_degree(erdos_renyi(i, (4/i))))
            maxs2.append(max_degree(barabasi_albert(i)))
        avg_maxs1.append((sum(maxs1)) / len(maxs1))
        avg_maxs2.append((sum(maxs2)) / len(maxs2))
    print(avg_maxs1)
    print(avg_maxs2)
    xax = []
    for i in range(1,100):
        xax.append(i)
    plt.plot(xax, avg_maxs1, label='Erdose Renyi')
    plt.plot(xax, avg_maxs2, label='Barabasi Albert')
    plt.xlabel('n')
    plt.ylabel('Average Maximum Degree')
    plt.title('N graph size vs average maximum degree')
    plt.legend()
    plt.show()