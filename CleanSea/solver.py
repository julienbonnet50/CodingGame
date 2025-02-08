import random
import matplotlib.pyplot as plt

def generate_naive_solution(M, N, nbBase, ocean_map):
    solution_map = [['>' for _ in range(N)] for _ in range(M)]  
    base_positions = []
    
    # Placer nbBase bases navales sur les premières cases contenant un déchet (X)
    for i in range(M):
        for j in range(N):
            if ocean_map[i][j] == 'X' and len(base_positions) < nbBase:
                # On alterne les directions des bases (Nord puis Est)
                direction = 'N' if len(base_positions) % 2 == 0 else 'E'
                solution_map[i][j] = direction
                base_positions.append((i, j))

    # Remplir le reste de la carte avec des directions aléatoires pour les déchets
    for i in range(M):
        for j in range(N):
            if (i, j) not in base_positions and ocean_map[i][j] == 'X':
                solution_map[i][j] = random.choice(['^', 'v', '<', '>'])

    return solution_map
