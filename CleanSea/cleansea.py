import random
import math
from utils import getFileNames, read_map_from_file, display_ocean_map, save_map_to_file, plot_maps
from solver import generate_naive_solution
from sklearn.cluster import KMeans
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

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


filename = "01_simple_example"
# filename = "02_small_sparse"
# filename = "03_medium"
# filename = "04_full"

inputPath, outputPath = getFileNames("C:\\Users\\julie\\Documents\\CodingGame\\CleanSea\\", filename+".txt")

# filename = r"C:\Users\julie\Documents\CodingGame\CleanSea\data\04_full.txt" 
posible_bases_favorites = ['N', 'E', 'S', 'W']
M, N, K, ocean_map = read_map_from_file(inputPath)
display_ocean_map(M, N, K, ocean_map)

solution_map = generate_naive_solution(M, N, K, ocean_map)
display_ocean_map(M, N, K, solution_map)
save_map_to_file(solution_map, outputPath)
plot_maps(ocean_map, solution_map, filename=filename)


