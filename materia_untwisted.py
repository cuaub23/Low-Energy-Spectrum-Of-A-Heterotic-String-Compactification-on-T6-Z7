import numpy as np
import itertools
from fractions import Fraction
import json


def suma_fracciones_pp(a, b):
    """
    Calcula el producto punto (producto escalar) entre dos vectores utilizando 
    fracciones para evitar errores de precisión de punto flotante.
    
    Entrada: a, b (listas o arrays de igual dimensión).
    Salida: Suma de la multiplicación entrada por entrada como un objeto Fraction o float.
    """
    suma_total = 0
    for i in range(len(a)):
        suma_total += Fraction(a[i]) * Fraction(b[i])
    return suma_total


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


def generar_vectores_q():
    """
    Genera los vectores 'q' correspondientes a los sectores Neveu-Schwarz (NS) y Ramond (R).
    
    Salida: Lista de vectores q generados.
    """
    q_vectors = []
    
    # Sector NS: Vectores con una sola entrada no nula (+1 o -1)
    for i in range(4):
        for s in [-1, 1]:
            v = [0, 0, 0, 0]
            v[i] = s
            q_vectors.append(v)

    # Sector R: Vectores con entradas +/- 0.5. 
    # Se impone la condición de paridad GSO (Gliozzi-Scherk-Olive) exigiendo un número par de signos positivos.
    for signs in itertools.product([-.5, .5], repeat=4):
        if signs.count(.5) % 2 == 0:
            q_vectors.append(list(signs))
            
    return q_vectors


def calcular_materia_cargada(sobrantes, q_vectors, v, twist, fases):
    """
    Filtra y agrupa las raíces candidatas (sobrantes) evaluando las condiciones de masa 
    y emparejamiento entre los vectores q (del sector bosónico) y el vector de twist,
    para cada fase generada por el orbifold.
    
    Salida: Lista de listas, donde cada sublista contiene los pares [vector_q, raiz_sobrante]
            que cumplen la condición para su fase correspondiente.
    """
    materia_cargada_4d = []
    
    # Precomputar los productos punto para optimizar el doble bucle
    a_valores = [suma_fracciones_pp(sobrante, v) for sobrante in sobrantes]
    b_valores = [suma_fracciones_pp(q, twist) for q in q_vectors]

    for fase in fases:
        materia_cargada_fase = []
        for i, b in enumerate(b_valores):
            # Selección del sector correspondiente según la fase actual
            if b == -fase:
                for j, a in enumerate(a_valores):
                    # Condición de supervivencia física: la diferencia (a - b) debe ser entera
                    n = a - b
                    if n % 1 == 0:
                        materia_cargada_fase.append([q_vectors[i], sobrantes[j]])
        materia_cargada_4d.append(materia_cargada_fase)
        
    return materia_cargada_4d


# =============================================================================
# BLOQUE DE EJECUCIÓN PRINCIPAL
# Todo el código dentro de este 'if' solo correrá si ejecutas este archivo directamente.
# =============================================================================
if __name__ == '__main__':
    # 1. Cargar archivos de datos generados previamente
    with open("raices_simples.json", "r") as f:
        raices_simples = json.load(f)
    with open('bosones.json', 'r') as f:
        bosones = json.load(f)
    with open('raices_no_inv.json', 'r') as f:
        sobrantes = json.load(f)

    # 2. Definición de los parámetros de desplazamiento y rotación del modelo
    v = [
        Fraction(2, 7), Fraction(2, 7), Fraction(1, 7), Fraction(1, 7), 
        Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7)
    ]
    twist = [0, Fraction(1, 7), Fraction(2, 7), Fraction(-3, 7)]
    fases = [
        Fraction(1, 7), Fraction(2, 7), Fraction(3, 7), 
        Fraction(4, 7), Fraction(5, 7), Fraction(6, 7)
    ]

    # 3. Construcción del modelo llamando a las funciones
    q_vectors = generar_vectores_q()
    materia_cargada_4d = calcular_materia_cargada(sobrantes, q_vectors, v, twist, fases)

    # 4. Impresión de resultados en consola
    for i in range(6): 
        print(f'Materia cargada con fase {fases[i]} \n Cantidad {len(materia_cargada_4d[i])}')
        for vector in materia_cargada_4d[i]:
            print(vector)
