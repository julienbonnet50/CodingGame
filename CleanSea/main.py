import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.dirname(p=__file__)))
from utils import getFileNames, read_map_from_file, display_ocean_map, save_map_to_file, plot_maps, simulate_score
from solver import generate_naive_solution

# filename = "01_simple_example"
# filename = "02_small_sparse"
# filename = "03_medium"
filename = "04_full"

inputPath, outputPath = getFileNames("C:\\Users\\julie\\Documents\\CodingGame\\CleanSea\\", filename+".txt")

# filename = r"C:\Users\julie\Documents\CodingGame\CleanSea\data\04_full.txt" 
posible_bases_favorites = ['N', 'E', 'S', 'W']
M, N, K, ocean_map = read_map_from_file(inputPath)
display_ocean_map(M, N, K, ocean_map)

solution_map = generate_naive_solution(M, N, K, ocean_map)
display_ocean_map(M, N, K, solution_map)
save_map_to_file(solution_map, outputPath)
plot_maps(ocean_map, solution_map, filename=filename)

print("Score : ", simulate_score(ocean_map, solution_map))

