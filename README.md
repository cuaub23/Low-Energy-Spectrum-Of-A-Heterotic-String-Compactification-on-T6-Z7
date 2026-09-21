# Low-Energy-Spectrum-Of-A-Heterotic-String-Compactification-on-T6-Z7

Dado dos vectores $v$ y $V$ que cumplan las siguientes condiciones: 
  
$$
\begin{align}
&7v \in \mathbb{Z}^3, \\
&v^1 + v^2 + v^3 = 0, \\
&7V \in \Gamma_{E_8 \times E_8}, \\
&7(V^2 - v^2) = 0 \ \text{mod} 2.
\end{align}
$$

Los programas calculan lo siguiente 
* El grupo de norma resultante de la compactificacion de la cuerda heterotica con grupo de norma $E_8 \times E_8$ en el orbifold $T^6/\mathbb{Z}_7$ con vector de desplazamiento $V$ y vector de torcimiento $v$.
- La materia cargada en la teoria 4D resultante en los sectores torcidos y no torcidos. 

> [!WARNING]
> Este programa calcula el espectro en el caso relevante para el que fue desarrollado en el que $V$ es de la siguiente forma:
>
> $$
> V=\frac{1}{7}(V_8)(0,0,0,0,0,0,0,0)
> $$
>
> con $V\in \Gamma_{E_8}$

## Raices de E8
Primeramente el programa `raicesE8.py` calcula las raices del grupo $E_8$ y genera un archivo JSON en donde las incluye. Las raices de este grupo son un conjunto de vectores descritos por las siguientes condiciones 

$$
 x \in \mathbb{R}^8 \ \bigg| \ \left( x \in \mathbb{Z}^8 \text{y} \sum_{i=1}^8 x_i \in 2\mathbb{Z} \right) \text{o}
 \left( x \in \left(\mathbb{Z} + \tfrac{1}{2}\right)^8 \text{y} \sum_{i=1}^8 x_i \in 2\mathbb{Z} \right) .
$$

Ademas 

$$
\sum_i x^i x^i = 2.
$$

## Bosones cargados 
Dado el vector de desplazamiento $V$ el programa `bosones.py` encuentra los bosones cargados de la teoria 4D resultante, siendo estos las raices $p$ de $E_8$ que cumplen 

$$
p \cdot V = 0 \ \text{mod} 1.
$$

El programa obtiene las raices del archivo previamente generado por `raicesE8.py` y arroja tres nuevos archivos:
* raices_simples.json en donde se encuentran las raices simples del conjunto de bosones cargados de la teoria 4D, siendo estas vectores que una vez definida una convencion de positividad (en este caso se dice que un vector es positivo si su primera entrada no cero es positiva) una raiz es simple si es positiva y su diferencia con otra raiz simple no es positiva.
* bosones.json en donde se encuentran los bosones cargados de la teoria 4D.
* raices_no_inv.json en donde se encuentran las raices de $E_8$ que no cumplen la condicion de invariancia anterior. 
## Materia cargada
El programa `materia_untwisted.py` encuentra los vectores de peso del grupo SO(8) siendo el siguiente conjunto $q$ de 16 vectores:

$$
q = 
\begin{cases}
&\underline{(\pm 1, 0, 0, 0 )} \\
&\left(\pm \frac{1}{2}, \pm \frac{1}{2}, \pm \frac{1}{2}, \pm \frac{1}{2} \right)
\end{cases},
$$

donde el subrayado denota todas las posibles permutaciones y los vectores fraccionarios tienen numero par de signos positivos.
Despues de esto obtiene la representacion en vectores de la materia cargada de la teoria en el sector no torcido, que consta del producto tensorial entre las raices $p$ y los vectores $q$ que cumplen 

$$
p \cdot V - q \cdot v = 0 \ \text{mod} 1.
$$

## Materia cargada de los sectores no torcidos 
La materia cargada del sector no torcido consta de los vectores $p\in\Gamma_{E_8}$ y $q\in\Gamma_{SO(8)}$ ($\Gamma_{SO(8)}$ la reticula de pesos de $SO(8)$) que satisfacen las siguientes condiciones 

$$
\begin{align}
(p + kV)^2 &= \frac{10}{7} -2 \tilde{N} \\
(q + kv)^2 &= \frac{3}{7}
\end{align}
$$

donde $k \in (1,2,3,4,5,6,7)$ y $\tilde{N}=\tfrac{n}{7}$ con $n\in(1,2,3,4,5)$.
> [!WARNING]
> Las ecuaciones anteriores son validas unicamente para $7v=(1,2,-3)$ o equivalentes fisicamente. En caso de que el vector $v$ cambie estas ecuaciones cambian. El programa sigue funcionando pero conduce a fisica incorrecta.

Los calculos de estos vectores se hacen en programas independientes

* `p_twist.py` genera vectores $p \in \Gamma_{E_8}$ y guarda aquellos que cumplan la condiciion anterior para los diferentes sectores torcidos etiquetados por $k$ y guarda el resultado en un archivo JSON.
* `q_twist.py` genera los vectores $q\in\Gamma_{SO(8)}$ que cumplen la condicion anterior e imprime el resultado en la terminal.
