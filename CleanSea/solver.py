import math
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.dirname(p=__file__)))
import random
from CleanSea.boat import Boat

def generate_naive_solution(M, N, nbBase, ocean_map):
    solution_map = [['>' for _ in range(N)] for _ in range(M)]  
    base_positions = []
    boats = []
    
    # place bases on the first 'X' positions
    for i in range(M):
        for j in range(N):
            if ocean_map[i][j] == 'X' and len(base_positions) < nbBase:
                # randomly choose a direction
                direction = 'N' if len(base_positions) % 2 == 0 else 'E'
                solution_map[i][j] = direction
                base_positions.append((i, j))
                boats.append(Boat(i, j, direction))

    # Randomly place travels directions
    for i in range(M):
        for j in range(N):
            if (i, j) not in base_positions and ocean_map[i][j] == 'X':
                solution_map[i][j] = random.choice(['^', 'v', '<', '>'])

    return solution_map

# Still WIP
def generate_solution_divided_by_n(M, N, K, ocean_map):
    # Initiate map with empty values
    solution_map = [[' ' for _ in range(N)] for _ in range(M)]

    # Place base entity
    base_positions = []
    posible_bases_favorites = ['N', 'O', 'S', 'E']
    rows_per_region = M // math.isqrt(K)
    cols_per_region = N // math.ceil(K / math.isqrt(K))
    for i in range(math.isqrt(K)):
        for j in range(math.ceil(K / math.isqrt(K))):
            if len(base_positions) >= K:
                break  # Stop once we have K bases

            center_row = min(M - 1, (i * rows_per_region) + (rows_per_region // 2))
            center_col = min(N - 1, (j * cols_per_region) + (cols_per_region // 2))
            solution_map[center_row][center_col] = random.choice(posible_bases_favorites)
            base_positions.append((center_row, center_col))

    # Find trash positions
    trash_positions = [(i, j) for i in range(M) for j in range(N) if ocean_map[i][j] == 'X']

    return solution_map