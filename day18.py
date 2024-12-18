from collections import deque

grid_size = 71
corrupted = []
for line in open("day18.input") :
    corrupted_line = line.strip().split(',')
    corrupted.append((int(corrupted_line[0]), int(corrupted_line[1])))

def shortest_path(corr, max_fallen_bytes):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, Bas, Gauche, Droite
    queue = deque([(0, 0, 0)])  # (ligne, colonne, distance)
    visited_or_corrupted = set(corr[:max_fallen_bytes])
    visited_or_corrupted.add((0,0))
    
    while queue:
        x, y, dist = queue.popleft()
        
        # Si on atteint le coin inférieur droit
        if (x, y) == (grid_size - 1, grid_size - 1):
            return dist
        
        # Explorer les voisins valides
        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited_or_corrupted :
                queue.append((nx, ny, dist + 1))
                visited_or_corrupted.add((nx, ny))
    
    return -1  # Pas de chemin possible

def part1() :
    print("part 1 : " + str(shortest_path(corrupted, 1024)))

def part2() :
    path = 0
    max = 1023
    while path > -1 :
        max += 1
        path = shortest_path(corrupted, max)
    print("part 2 : " + str(corrupted[max-1]))

part1()
part2()
