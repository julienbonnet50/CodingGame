import random

def generate_naive_solution(M, N, nbBase, ocean_map):
    solution_map = [['>' for _ in range(N)] for _ in range(M)]  
    base_positions = []
    
    # place bases on the first 'X' positions
    for i in range(M):
        for j in range(N):
            if ocean_map[i][j] == 'X' and len(base_positions) < nbBase:
                # randomly choose a direction
                direction = 'N' if len(base_positions) % 2 == 0 else 'E'
                solution_map[i][j] = direction
                base_positions.append((i, j))

    # Randomly place travels directions
    for i in range(M):
        for j in range(N):
            if (i, j) not in base_positions and ocean_map[i][j] == 'X':
                solution_map[i][j] = random.choice(['^', 'v', '<', '>'])

    return solution_map
