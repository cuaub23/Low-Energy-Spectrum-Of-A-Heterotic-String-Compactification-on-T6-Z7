import numpy as np
from itertools import product

valores = [-1.5, -0.5, 0.5, 1.5]
v_twist = np.array([0, 1/7, 2/7, -3/7])
k = 3
shift = k * v_twist

for q in product(valores, repeat=4):
    q = np.array(q)
    if abs(sum(q) % 2) < 1e-5: 
        q_sh = q + shift
        norma = np.dot(q_sh, q_sh)     
        if abs(norma - 3/7) < 1e-5:
            print(f"¡Encontrado! q={q}, q_sh={q_sh}, norma={norma:.4f}")