import json
from fractions import Fraction
import numpy as np


def producto_punto_frac(a, b):
    """
    Calcula el producto punto entre dos vectores utilizando fracciones para evitar 
    errores de punto flotante.
    
    Entrada: a, b (listas o arrays de igual dimensión).
    Salida: Suma de sus entradas como un objeto Fraction.
    """
    sum = 0
    for i in range(len(a)):
        sum += Fraction(a[i]) * Fraction(b[i])
    return sum


def suma(a, b):
    """
    Suma dos vectores entrada por entrada utilizando formato de fracción.
    
    Entrada: a, b (listas o arrays de igual dimensión).
    Salida: Lista con la suma fraccionaria de los elementos correspondientes.
    """
    c = []
    for i in range(len(a)):
        c.append(Fraction(a[i]) + Fraction(b[i]))
    return c


def cartan_matrix(simple_roots):
    """
    Calcula la matriz de Cartan (A_ij = 2 * a_i * a_j / a_j^2) de un conjunto de raíces simples.
    
    Entrada: simple_roots (lista o array de vectores de dimensión n).
    Salida: Array NumPy de dimensión (n,n) que representa la matriz de Cartan.
    """
    simple_roots = np.array(simple_roots)
    n = len(simple_roots)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = 2 * np.dot(simple_roots[i], simple_roots[j]) / np.dot(
                simple_roots[j], simple_roots[j]
            )
    return A


def simple_roots(roots):
    """
    Encuentra las raíces simples de un conjunto de raíces. Una raíz simple es aquella 
    que es positiva y no puede expresarse como la suma de otras dos raíces positivas.
    (Un vector es positivo si su primera entrada no nula es mayor a cero).
    
    Entrada: roots (lista o array de m vectores de dimensión n).
    Salida: Array con las raíces simples encontradas.
    """
    roots = np.array(roots, dtype=float)
    mask = np.zeros(len(roots), dtype=bool)
    
    # 1. Identificar raíces positivas
    for i, r in enumerate(roots):
        for component in r:
            if component != 0:
                mask[i] = (component > 0)
                break
                
    positive = roots[mask]
    n = len(positive)

    # 2. Búsqueda de raíces simples por diferencias
    positive_set = {tuple(np.round(r, 8)) for r in positive}
    diffs = positive[:, np.newaxis, :] - positive[np.newaxis, :, :]
    diffs_rounded = np.round(diffs, 8)

    simple = []
    for i, p in enumerate(positive):
        es_simple = True
        for j in range(n):
            if i != j:  # No comparar la raíz consigo misma
                diff_tuple = tuple(diffs_rounded[i, j])
                # Si la diferencia resulta ser otra raíz positiva, se descarta
                if diff_tuple in positive_set:
                    es_simple = False
                    break
        if es_simple:
            simple.append(p)
            
    return np.array(simple)


def raices_inv_and_noinv(V, raices):
    """
    Filtra las raíces encontrando los bosones 4D (aquellas raíces cuyo producto punto 
    con el vector de desplazamiento V es cero módulo 1).
    
    Entrada: V (vector de desplazamiento), raices (conjunto de raíces E8).
    Salida: Tupla con (bosones_4d, matter_4d_candidates).
    """
    bosones_4d = []
    matter_4d_candidates = []

    for raiz in raices:
        # La condición módulo 1 se cumple si el denominador de la fracción resultante es 1
        if producto_punto_frac(raiz, V).denominator == 1:
            bosones_4d.append(raiz)
        else:
            matter_4d_candidates.append(raiz)
            
    return bosones_4d, matter_4d_candidates


# =============================================================================
# BLOQUE DE EJECUCIÓN PRINCIPAL
# Todo el código dentro de este 'if' solo correrá si ejecutas este archivo directamente.
# Si en el futuro importas 'cartan_matrix' en otro script, nada de esto se ejecutará.
# =============================================================================
if __name__ == '__main__':
    # Importar el archivo generado previamente
    with open("raices_e8.json", "r") as f:
        raices_e8 = json.load(f)

    # Definición del vector de desplazamiento
    V = [
        Fraction(2, 7), Fraction(2, 7), Fraction(1, 7), Fraction(1, 7),
        Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7),
    ]

    # Ejecución de la lógica principal
    bosones_4d, matter_4d_candidates = raices_inv_and_noinv(V, raices_e8)
    raices_simples = simple_roots(bosones_4d)

    # Resultados por consola
    print("Numero de raices simples:", len(raices_simples))
    print("Raices simples:")
    for raiz in raices_simples:
        print(raiz)
        
    print("Matriz de Cartan:")
    print(cartan_matrix(raices_simples))

    # Generación de archivos JSON de salida
    with open("raices_simples.json", "w") as f:
        json.dump(raices_simples.tolist(), f)
        
    with open("bosones.json", "w") as f:
        json.dump(bosones_4d, f)
        
    with open("raices_no_inv.json", "w") as f:
        json.dump(matter_4d_candidates, f)
