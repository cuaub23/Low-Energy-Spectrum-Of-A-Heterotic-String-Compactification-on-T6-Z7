import numpy as np
from fractions import Fraction
import json

with open("raices_e8.json", "r") as f:
    raices_e8 = json.load(f)

def producto_punto_frac(a, b):
  sum = 0
  for i in range(len(a)):
    sum += Fraction(a[i])*Fraction(b[i])
  return sum

def suma(a, b):
   c = []
   for i in range(len(a)):
      c.append(Fraction(a[i]) + Fraction(b[i]))
   return c 

def cartan_matrix(simple_roots):
    simple_roots = np.array(simple_roots)
    n = len(simple_roots)
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = 2*np.dot(simple_roots[i], simple_roots[j]) / np.dot(simple_roots[j], simple_roots[j])
    return A

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

bosones_4d = []
matter_4d_candidates = []
v = [Fraction(2, 7), Fraction(2, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), 
    Fraction(1, 7)]
for raiz in raices_e8:
    if producto_punto_frac(raiz, v) == 0:
        bosones_4d.append(raiz)
    else: 
        matter_4d_candidates.append(raiz)
        

raices_simples = simple_roots(bosones_4d)

print('Numero de raices simples:', len(bosones_4d))
print('Raices simples:')
for raiz in raices_simples:
   print(raiz)
print('Matriz de Cartan:')
print(cartan_matrix(raices_simples))

with open("raices_simples.json", "w") as f:
    json.dump(raices_simples.tolist(), f)
with open('bosones.json', 'w') as f:
    json.dump(bosones_4d, f)
with open('raices_no_inv.json', 'w') as f:
    json.dump(matter_4d_candidates, f)

'''
#Tabla latex bosones con raices enteras

c = 0
for i in range(32):
    if c == 0:
      print('$', end='')
    c+=1
    print(f'({int(bosones[i][0])}, {int(bosones[i][1])}, {int(bosones[i][2])}, {int(bosones[i][3])}, {int(bosones[i][4])}, {int(bosones[i][5])}, {int(bosones[i][6])}, {int(bosones[i][7])}), ', end='')
    if c==4:
      print('$ \\\\')
      c = 0

#Tabla latex bosones con raices de entradas semi enteras

c = 0
for i in range(32, len(bosones)):
    for j in range(8):
      if bosones[i][j] == 0.5: bosones[i][j] = '\\frac{1}{2}'
      elif bosones[i][j] == -0.5: bosones[i][j] = '-\\frac{1}{2}'
    if c == 0:
        print('$', end='')
    c+= 1
    print(f'({bosones[i][0]},{bosones[i][1]},{bosones[i][2]},{bosones[i][3]},{bosones[i][4]},{bosones[i][5]},{bosones[i][6]},{bosones[i][7]}),', end='')
    if c==3:
        print('$ \\\\')
        c = 0
'''