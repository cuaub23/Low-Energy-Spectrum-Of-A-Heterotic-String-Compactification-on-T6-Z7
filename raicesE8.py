import numpy as np
import itertools
import json

def generate_e8_roots():
    """
    Genera las 240 raíces del grupo de Lie E8.
    
    El conjunto de raíces de E8 consta de:
    1. 112 vectores con entradas enteras (dos entradas con +/-1 y el resto 0).
    2. 128 vectores con entradas semienteras (+/-0.5) y un número par de signos negativos.
    
    Returns:
        np.ndarray: Array de dimensión (240, 8) que contiene todas las raíces.
    """
    roots = []
    
    # 1. Generar vectores con entradas enteras (+/-1, +/-1, 0, 0, 0, 0, 0, 0)
    for i, j in itertools.combinations(range(8), 2):
        for sign_i, sign_j in itertools.product([1, -1], repeat=2):
            root = np.zeros(8)
            root[i] = sign_i
            root[j] = sign_j
            roots.append(root)
            
    # 2. Generar vectores con entradas semienteras (+/-0.5) con número par de signos negativos
    for signs in itertools.product([0.5, -0.5], repeat=8):
        if signs.count(-0.5) % 2 == 0:
            roots.append(np.array(signs))

    return np.array(roots)

if __name__ == "__main__":
    # Ejecución principal para generar y guardar el archivo JSON
    raices_e8 = generate_e8_roots()
    
    with open('raices_e8.json', 'w') as f:
        json.dump(raices_e8.tolist(), f)
