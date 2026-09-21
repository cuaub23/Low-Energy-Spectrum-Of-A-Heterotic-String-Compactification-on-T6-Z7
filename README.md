# Low-Energy-Spectrum-Of-A-Heterotic-String-Compactification-on-T6-Z7

Dados dos vectores $v$ y $V$ que cumplan las siguientes condiciones: 
  
$$\begin{align} 
&7v \in \mathbb{Z}^3, \\ 
&v^1 + v^2 + v^3 = 0, \\ 
&7V \in \Gamma_{E_8 \times E_8}, \\ 
&7(V^2 - v^2) = 0 \ \text{mod} 2. 
\end{align}$$

Los programas calculan lo siguiente:
* El grupo de norma resultante de la compactificación de la cuerda heterótica con grupo de norma $E_8 \times E_8$ en el orbifold $T^6/\mathbb{Z}_7$ con vector de desplazamiento $V$ y vector de torcimiento $v$.
* La materia cargada en la teoría 4D resultante en los sectores torcidos y no torcidos.

## Tecnologías Usadas
* **Python**: Lenguaje principal.
* **NumPy**: Para el manejo eficiente de arrays.
* **Itertools**: Para la generación de productos cartesianos.
* **SciPy**: Para encontrar vectores que cumplan las condiciones deseadas dentro de un gran conjunto. 

> [!WARNING]
> Este programa calcula el espectro en el caso relevante para el que fue desarrollado, en el que $V$ es de la siguiente forma:
>
> $$ V=\frac{1}{7}(V_8)(0,0,0,0,0,0,0,0) $$
>
> con $V\in \Gamma_{E_8}$.

## Raíces de E8
Primero, el programa `raicesE8.py` calcula las raíces del grupo $E_8$ y genera un archivo JSON en donde las incluye. Las raíces de este grupo son un conjunto de vectores descritos por las siguientes condiciones: 

$$x \in \mathbb{R}^8 \ \bigg\vert{} \ \left( x \in \mathbb{Z}^8 \text{ y } \sum_{i=1}^8 x_i \in 2\mathbb{Z} \right) \text{o }  \left( x \in \left(\mathbb{Z} + \tfrac{1}{2}\right)^8 \text{ y } \sum_{i=1}^8 x_i \in 2\mathbb{Z} \right).$$

Además: 

$$\sum_i x^i x^i = 2.$$

## Bosones cargados 
Dado el vector de desplazamiento $V$, el programa `bosones.py` encuentra los bosones cargados de la teoría 4D resultante, siendo estos las raíces $p$ de $E_8$ que cumplen: 

$$p \cdot V = 0 \ \text{mod} 1.$$

El programa obtiene las raíces del archivo previamente generado por `raicesE8.py` y arroja tres nuevos archivos:
* `raices_simples.json`: en donde se encuentran las raíces simples del conjunto de bosones cargados de la teoría 4D. Una vez definida una convención de positividad (en este caso se dice que un vector es positivo si su primera entrada no cero es positiva), una raíz es simple si es positiva y su diferencia con otra raíz simple no es positiva.
* `bosones.json`: en donde se encuentran los bosones cargados de la teoría 4D.
* `raices_no_inv.json`: en donde se encuentran las raíces de $E_8$ que no cumplen la condición de invariancia anterior. 

## Materia cargada
El programa `materia_untwisted.py` encuentra los vectores de peso del grupo $SO(8)$, siendo el siguiente conjunto $q$ de 16 vectores:

$$q =  \begin{cases} &\underline{(\pm 1, 0, 0, 0 )} \\ &\left(\pm \frac{1}{2}, \pm \frac{1}{2}, \pm \frac{1}{2}, \pm \frac{1}{2} \right) \end{cases},$$

donde el subrayado denota todas las posibles permutaciones y los vectores fraccionarios tienen número par de signos positivos.
Después de esto, obtiene la representación en vectores de la materia cargada de la teoría en el sector no torcido, que consta del producto tensorial entre las raíces $p$ y los vectores $q$ que cumplen: 

$$p \cdot V - q \cdot v = 0 \ \text{mod} 1.$$

## Materia cargada de los sectores torcidos 
La materia cargada del sector torcido consta de los vectores $p\in\Gamma_{E_8}$ y $q\in\Gamma_{SO(8)}$ (siendo $\Gamma_{SO(8)}$ la retícula de pesos de $SO(8)$) que satisfacen las siguientes condiciones: 

$$\begin{align} (p + kV)^2 &= \frac{10}{7} -2 \tilde{N} \\ (q + kv)^2 &= \frac{3}{7} \end{align}$$

donde $k \in (3,5,6)$  y $\tilde{N}=\tfrac{n}{7}$ con $n\in(1,2,3,4,5)$.

> [!WARNING]
> Las ecuaciones anteriores son válidas únicamente para $7v=(1,2,-3)$ o equivalentes físicamente. En caso de que el vector $v$ cambie, estas ecuaciones cambian. El programa sigue funcionando pero conduce a física incorrecta. Por lo que el único parámetro libre para estos programas es $V$.

Los cálculos de estos vectores se hacen en programas independientes:
* `p_twist.py` genera vectores $p \in \Gamma_{E_8}$ y guarda aquellos que cumplan la condición anterior para los diferentes sectores torcidos etiquetados por $k$, guardando el resultado en un archivo JSON.
* `q_twist.py` genera los vectores $q\in\Gamma_{SO(8)}$ que cumplen la condición anterior e imprime el resultado en la terminal.

## Resultados 
El programa se utilizó para el desarrollo de la tesis de investigación [El MSSM a partir del orbifold heterótico Z7](). El vector $V$ se eligió ser: 

$$V=\frac{1}{7}(2,2,1,1,1,1,1,1)(0^8)$$

donde se obtuvo lo siguiente:

> [!IMPORTANT]
> * 240 raíces de $E_8$, como es matemáticamente correcto.
> * 72 bosones cargados en la teoría 4D.
> * 6 raíces simples. 
> * Una matriz de Cartan A que corresponde a $E_6$.
> * Los siguientes vectores $p$ en el sector torcido: 27 vectores $p$ para $k=3,5,6$ y $\tilde{N}=0$; 1 vector $p$ para $k=3,5,6$ y $\tilde{N}=\tfrac{1}{7}$; 1 vector $p$ para $k=3,5,6$ y $\tilde{N}=\tfrac{2}{7}$; y 1 vector $p$ para $k=3,5,6$ y $\tilde{N}=\tfrac{4}{7}$.
> * 3 vectores $q$ en el sector torcido.

## Ejecución 
Para ejecutar los scripts localmente, se necesita tener instalados los paquetes `numpy` y `scipy`. 

Los programas `raicesE8.py`, `bosones.py` y `materia_untwisted.py` se deben ejecutar en ese orden. Mientras tanto, `p_twist.py` y `q_twist.py` se pueden ejecutar en cualquier momento.
