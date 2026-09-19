import numpy as np
import itertools
from sympy import Matrix
import json

def generate_e8_roots_numpy():
    roots_list = []
    for i, j in itertools.combinations(range(8), 2):
        for sign_i in [1, -1]:
            for sign_j in [1, -1]:
                root = np.zeros(8)
                root[i] = sign_i
                root[j] = sign_j
                roots_list.append(root)
    for signs in itertools.product([0.5, -0.5], repeat=8):
        if list(signs).count(-0.5) % 2 == 0:
            roots_list.append(np.array(signs))

    return np.array(roots_list)

def simple_roots(roots):
    roots = np.array(roots, dtype=float)
    mask = np.zeros(len(roots), dtype=bool)
    for i, r in enumerate(roots):
        for component in r:
            if component != 0:
                mask[i] = (component > 0)
                break
    positive = roots[mask]
    n = len(positive)

    positive_set = {tuple(np.round(r, 8)) for r in positive}
    diffs = positive[:, np.newaxis, :] - positive[np.newaxis, :, :]
    diffs_rounded = np.round(diffs, 8)

    simple = []
    for i, p in enumerate(positive):
        es_simple = True
        for j in range(n):
            if i != j:  # No comparar consigo mismo
                diff_tuple = tuple(diffs_rounded[i, j])
                if diff_tuple in positive_set:
                    es_simple = False
                    break
        if es_simple:
            simple.append(p)
    return np.array(simple)

def cartan_matrix(simple_roots):
    simple_roots = np.array(simple_roots)
    n = len(simple_roots)
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = 2*np.dot(simple_roots[i], simple_roots[j]) / np.dot(simple_roots[j], simple_roots[j])
    return A


raicese8 = generate_e8_roots_numpy()
with open('raices_e8.json', 'w') as f:
    json.dump(raicese8.tolist(), f)