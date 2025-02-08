import matplotlib.pyplot as plt
import numpy as np

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

def plot_maps(ocean_map, solution_map, base_positions=None, cell_size=0.5, 
              max_fig_width=20, max_fig_height=20, text_threshold=1000000):
    """
    Displays the ocean map and the solution map, adapting the figure size to large maps.
    
    Parameters:
      - ocean_map: list of strings (each row), where 'X' represents a debris and '.' water.
      - solution_map: list of strings (each row), containing either base letters ('N','O','S','E')
                      or movement instructions ('^','v','<','>').
      - base_positions: (optional) list of (i, j) tuples indicating base positions.
                        If provided, these positions will be marked even if solution_map does not contain base letters.
      - cell_size: size of each cell in inches.
      - max_fig_width, max_fig_height: maximum size of the figure in inches.
      - text_threshold: maximum number of cells for which to draw text (to avoid clutter).
    """
    M = len(ocean_map)
    N = len(ocean_map[0])
    
    # Calculate ideal figure size
    ideal_width = N * cell_size
    ideal_height = M * cell_size
    fig_width = min(ideal_width, max_fig_width)
    fig_height = min(ideal_height, max_fig_height)
    
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    # Create an RGB image: red for debris, blue for water
    ocean_grid = np.zeros((M, N, 3))
    for i in range(M):
        for j in range(N):
            if ocean_map[i][j] == 'X':
                ocean_grid[i, j] = [1, 0, 0]  # Red for debris
            else:
                ocean_grid[i, j] = [0, 0, 1]  # Blue for water

    # Display the ocean map; extent is set so that cells align nicely
    ax.imshow(ocean_grid, interpolation='none', extent=[0, N, M, 0])
    
    # Decide whether to draw text (if the grid is not too crowded)
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
                # If the cell has another character (or blank), no text is drawn.
    
    # If no base letters are present in solution_map, but you have base positions,
    # mark them with a circle (or another marker)
    if base_positions is not None:
        for (i, j) in base_positions:
            # Draw a white circle at the center of the cell
            ax.plot(j + 0.5, i + 0.5, marker='o', color='white', markersize=cell_size * 10, markeredgewidth=2)
    
    # Draw grid lines
    ax.set_xticks(np.arange(0, N + 1, 1))
    ax.set_yticks(np.arange(0, M + 1, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which='both', color='black', linestyle='-', linewidth=0.5)
    
    plt.show()