import numpy as np
import itertools
from fractions import Fraction
import json

with open("raices_simples.json", "r") as f:
    raices_simples = json.load(f)
with open('bosones.json', 'r') as f:
    bosones = json.load(f)
with open('raices_no_inv.json', 'r') as f:
    sobrantes = json.load(f)

def suma_fracciones_pp(a, b):
  sum = 0
  for i in range(len(a)):
    sum += Fraction(a[i])*b[i]
  return sum

def suma(a, b):
   c = []
   for i in range(len(a)):
      c.append(Fraction(a[i]) + Fraction(b[i]))
   return c 

q_vectors = [] #Vectores q

for i in range(4): #Sector NS
    for s in [-1, 1]:
        v = [0,0,0,0]
        v[i] = s
        q_vectors.append(v)

for signs in itertools.product([-.5, .5], repeat=4): #Sector R
    if signs.count(.5) % 2 == 0:   # par de +'s
        q_vectors.append(list(signs))

v = [Fraction(2, 7), Fraction(2, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), Fraction(1, 7), 
    Fraction(1, 7)]
twist = [0, Fraction(1, 7), Fraction(2, 7), Fraction(-3, 7)]

materia_cargada_4d = []

fases = [Fraction(1, 7), Fraction(2, 7), Fraction(3, 7), Fraction(4, 7), Fraction(5, 7), Fraction(6, 7)]
materia_cargada_4d = []

a_valores = [suma_fracciones_pp(sobrante, v) for sobrante in sobrantes]
b_valores = [suma_fracciones_pp(q, twist) for q in q_vectors]

for fase in fases:
    materia_cargada_fase = []
    for i, b in enumerate(b_valores):
        if b == -fase:
            for j, a in enumerate(a_valores):
                n = a - b
                if n % 1 == 0:
                    materia_cargada_fase.append([q_vectors[i], sobrantes[j]])
    materia_cargada_4d.append(materia_cargada_fase)

for i in range(6): 
    print(f'Materia cargada con fase {fases[i]} \n Cantidad {len(materia_cargada_4d[i])}')
    for vector in materia_cargada_4d[i]:
        print(vector)

'''
#representaciones U

t1 = [Fraction(7, 2), Fraction(7, 2), 0, 0, 0, 0, 0, 0]
t2 = [0, 0, Fraction(7, 2), Fraction(7, 2), Fraction(7, 2), Fraction(7, 2), Fraction(7, 2), Fraction(7, 2)]

cargas = []
cargas_dif = []
for materia in sobrantes: 
    c1 = suma_fracciones_pp(materia, t1)
    c2 = suma_fracciones_pp(materia, t2)
    c = (c1, c2)
    cargas.append(c)
    if c not in cargas_dif:
        cargas_dif.append(c)

for carga in cargas_dif:
    print(carga, cargas.count(carga))    
'''

'''
#Materia cargada vectores
f = 2
print(f'Fase {f+1}/7')
for materia in materia_cargada_4d:
    print(len(materia))
q = materia_cargada_4d[f][0][0]
print(q)
c = 0
for i in range(len(materia_cargada_4d[f])):
    p = materia_cargada_4d[f][i][1].copy()
    if q == materia_cargada_4d[f][i][0]:
        if c == 2: 
            print('$ \\\ ') 
            print(end="& & $") 
            c = 0 
        for k in range(len(p)):
            if p[k] == 0.5 : p[k] = '\\' + 'frac{1}{2}'
            elif p[k] == -0.5 : p[k] = '-\\' + 'frac{1}{2}'
            elif p[k]%1 == 0 : p[k] = int(p[k]) 
        print(f'( {p[0]}, {(p[1])}, {p[2]}, {p[3]}, {p[4]}, {p[5]}, {p[6]}, {p[7]})', end=",") 
        c += 1
    else:
        print('')
        print('Cambio de q', c)
        c = 0 
        q = materia_cargada_4d[f][i][0]
        for k in range(len(p)):
            if p[k] == 0.5 : p[k] = '\\' + 'frac{1}{2}'
            elif p[k] == -0.5 : p[k] = '-\\' + 'frac{1}{2}'
            elif p[k]%1 == 0 : p[k] = int(p[k]) 
        print(f'( {p[0]}, {(p[1])}, {p[2]}, {p[3]}, {p[4]}, {p[5]}, {p[6]}, {p[7]})', end=",") 
print('\n', q)
'''

'''
#representaciones grupo no abeliano
representaciones = []
for sobrante in sobrantes: 
    f = [0]*8
    for i in range(len(raices_simples)):
        a = suma_fracciones_pp(sobrante, raices_simples[i])
        f[i] = a
    representaciones.append(f)

#print(representaciones)
repres_ind = []
for i in range(len(representaciones)):
    if representaciones[i] not in repres_ind: 
        repres_ind.append(representaciones[i])
print(len(representaciones))

repres_ind_pos = []
for repre_ind in repres_ind: 
    a = (-1)*np.array(repre_ind)
    a = a.tolist()
    if a not in repres_ind_pos:
        repres_ind_pos.append(repre_ind)
    
print(len(repres_ind_pos))
print(repres_ind_pos)

for r in repres_ind_pos:
    d = f'({int(r[0])}, {int(r[1])}, {int(r[2])}, {int(r[3])}, {int(r[4])}, {int(r[5])}, {int(r[6])}, {int(r[7])})'
    print(f'${d}$ & 3 & $-{d}$ & 3 \\\\ \\hline')
'''