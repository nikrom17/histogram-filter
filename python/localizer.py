# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs= [[] * len(beliefs[0]) for i in range(len(beliefs))]
    s = 0 
    for i in range(len(beliefs)):
        for j in range(len(beliefs[0])):
            hit = (color == grid[i][j])
            p = beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss)
            new_beliefs[i].append(p)
            s += p;
    for i in range(len(beliefs)):
        for j in range(len(beliefs)):
            new_beliefs[i][j] /= s          
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(height)] for j in range(width)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            print('i: ')
            print(i)
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            # pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)
