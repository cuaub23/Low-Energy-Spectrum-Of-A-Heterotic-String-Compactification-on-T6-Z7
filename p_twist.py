import itertools
import numpy as np
import json
from scipy.spatial import cKDTree

def buscar_espectro_e8  (V_shift, targets_norm, k_sector=1, tolerancia=1e-5):
    """Usa árbol KD para búsqueda de vecinos cercanos (muy escalable)."""
    V_eff = k_sector * np.array(V_shift)
    
    rango_base = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    
    # Generar puntos válidos
    puntos = []
    for es_entero in [True, False]:
        rango = rango_base[rango_base % 1 == 0] if es_entero else rango_base[rango_base % 1 == 0.5]
        for p in itertools.product(rango, repeat=8):
            p = np.array(p)
            if int(np.sum(p)) % 2 == 0:
                puntos.append(p + V_eff)
    
    puntos = np.array(puntos)
    
    # Calcular normas
    normas_sq = np.sum(puntos**2, axis=1)
    targets_array = np.array(targets_norm).reshape(-1, 1)
    
    # KDTree en espacio 1D de normas
    tree = cKDTree(normas_sq.reshape(-1, 1))
    indices = tree.query_ball_point(targets_array, tolerancia)
    
    encontrados = []
    for target, idx_list in zip(targets_norm, indices):
        for idx in idx_list:
            encontrados.append([puntos[idx].tolist(), normas_sq[idx]])
    
    return encontrados

v = [2/7, 2/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]
objetivos = [10/7, 8/7, 6/7, 4/7, 2/7, 0]  
k = 5
resultados = buscar_espectro_e8(v, objetivos, k)

print(len(resultados))

with open (f'p_twist_k{k}.json', 'w') as f:
    json.dump(resultados, f)