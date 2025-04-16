'''
Ben Frederick
CS 1210
'''
ROUTES = {
        'Burlington': ['St Albans', 'Montpelier', 'Middlebury'],
        'Montpelier': ['Burlington', 'White River Junction', 'St Johnsbury'],
        'White River Junction': ['Montpelier', 'Brattleboro', 'St Johnsbury'],
        'Brattleboro': ['White River Junction'],
        'Newport': ['St Johnsbury'],
        'St Albans': ['Burlington', 'Swanton'],
        'St Johnsbury': ['Montpelier', 'White River Junction', 'Newport'],
        'Swanton': ['St Albans'],
        'Middlebury': ['Burlington', 'Rutland'],
        'Rutland': ['Middlebury', 'Bennington'],
        'Bennington': ['Rutland']
}

def bfs(adj, key):
    nodes = []
    if key not in adj:
        return nodes
    visited = []
    q = [key]
    while q:
        thing = q.pop(0)
        if thing not in visited:
            visited.append(thing)
            nodes.append(thing)
            for i in adj[thing]:
                if i not in visited:
                    q.append(i)
    return nodes