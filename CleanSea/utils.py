import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.dirname(p=__file__)))
import copy
import matplotlib.pyplot as plt
import numpy as np
import os
import time
from CleanSea.boat import Boat

def save_map_to_file(solution_map, outputPath):
    converted_map = []
    for row in solution_map:
        converted_row = ''.join(row)
        converted_map.append(converted_row)

    with open(outputPath, 'w') as file:
        for row in converted_map:
            file.write(row + "\n")

def read_map_from_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        M, N, K = map(int, first_line.split())
        ocean_map = [list(file.readline().strip()) for _ in range(M)]
    return M, N, K, ocean_map


def display_ocean_map(M, N, K, ocean_map, raw_output=False):
    if raw_output:
        for row in ocean_map:
            print("".join(row))
        return

    print(f" 🌍 Dimensions : {M} x {N} | ⚓ Bases navales : {K}\n")

    print("    " + "".join(f"{j:2}" for j in range(N)))  
    print("    _" + "_" * (N * 2)) 

    for i, row in enumerate(ocean_map):
        print(f"{i:2} | " + " ".join(row) + " |")

    print("   +" + "-" * (N * 2 + 1) + "+ \n") 


def getFileNames(initPath, filename):
    outputPath = initPath + "output" + "\\" + filename 
    inputPath = initPath + "data" + "\\" + filename 
    return inputPath, outputPath

def plot_maps(ocean_map, solution_map, filename ,base_positions=None, cell_size=0.5, 
              max_fig_width=20, max_fig_height=20, text_threshold=100000, show=False):
    
    M = len(ocean_map)
    N = len(ocean_map[0])
    ideal_width = N * cell_size
    ideal_height = M * cell_size
    fig_width = min(ideal_width, max_fig_width)
    fig_height = min(ideal_height, max_fig_height)
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ocean_grid = np.zeros((M, N, 3))
    
    for i in range(M):
        for j in range(N):
            if ocean_map[i][j] == 'X':
                ocean_grid[i, j] = [1, 0, 0]
            else:
                ocean_grid[i, j] = [0, 0, 1]
    
    ax.imshow(ocean_grid, interpolation='none', extent=[0, N, M, 0])
    
    if M * N <= text_threshold:
        font_size = max(8, cell_size * 12)
        for i in range(M):
            for j in range(N):
                char = solution_map[i][j]
                if char in ['N', 'O', 'S', 'E']:
                    ax.text(j + 0.5, i + 0.5, char, ha='center', va='center', 
                            color='white', fontsize=font_size, fontweight='bold')
                elif char in ['^', 'v', '<', '>']:
                    ax.text(j + 0.5, i + 0.5, char, ha='center', va='center', 
                            color='yellow', fontsize=font_size, fontweight='bold')
    
    if base_positions is not None:
        for (i, j) in base_positions:
            ax.plot(j + 0.5, i + 0.5, marker='o', color='white', markersize=cell_size * 10, markeredgewidth=2)
    
    ax.set_xticks(np.arange(0, N + 1, 1))
    ax.set_yticks(np.arange(0, M + 1, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which='both', color='black', linestyle='-', linewidth=0.5)
    
    timestamp = int(time.time())
    filename = f"CleanSea/output/plot/{filename}-{timestamp}.png"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    if show:
        plt.show()

def simulate_score(debris_grid, config_grid, days=1000, show=True):

    # Init consts & variables
    M = len(config_grid)
    N = len(config_grid[0])
    score = 0  
    debris = [list(row) for row in debris_grid]
    boats = []
    directions = {
        'N': (-1, 0), 'O': (0, -1), 'S': (1, 0), 'E': (0, 1),
        '^': (-1, 0), '<': (0, -1), 'v': (1, 0), '>': (0, 1)
    }
    
    # Init boats on base bositions with preferedPosition and little name
    for i in range(M):
        for j in range(N):
            if config_grid[i][j] in "NOSE":
                boats.append(Boat(i, j, preferedPosition=config_grid[i][j], number=len(boats)))
    
    # Lets iterate over days
    for day in range(days):

        # --- Step 0 : Count boats on each cell
        pos_counts = {} 
        for boat in boats:
            pos = (boat.x, boat.y)
            pos_counts[pos] = pos_counts.get(pos, 0) + 1
        
        # --- Step 1 : Count debris on boat cell and add it
        for boat in boats:
            if boat.debrisCount < 2 and debris[boat.x][boat.y] == 'X':
                boat.debrisCount += 1

                # Delete debris from grid
                debris[boat.x][boat.y] = '.'

            if config_grid[boat.x][boat.y] in "NOSE":
                score += boat.debrisCount
                boat.debrisCount = 0

        # --- Step 2 : Move boats
        for boat in boats:
            # If boat is on a base or cell is already occuped, boat moves in prefered position
            if config_grid[boat.x][boat.y] in "NOSE" or pos_counts[(boat.x, boat.y)] > 1:
                move_char = boat.preferedPosition
            else:
                move_char = config_grid[boat.x][boat.y]
            
            dx, dy = directions[move_char]

            # Transpose position to top when it goes out of map
            boat.x = (boat.x + dx) % M
            boat.y = (boat.y + dy) % N
        
        # --- Step 3 : Print map with boats (only if show == True)
        if show:
            grid_boats= copy.deepcopy(config_grid)
            for boat in boats:
                grid_boats[boat.x][boat.y] = boat.name

    return score