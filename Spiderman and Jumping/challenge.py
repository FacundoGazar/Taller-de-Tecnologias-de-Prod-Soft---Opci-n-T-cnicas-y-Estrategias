import sys
from math import log2

# EL PEOR EJERCICIO DE TODA LA MATERIA, LO ODIE

def minimal_energy(N, heights):
    '''
        Calcula el costo minimo de energia entre saltos que pesan para indices que son **2 
    '''
    DP = [10 ** 9] * N   # Ponemos que el valor minimo de todas las posiciones es el valor maximo de las alturas segun el ejercicio
    DP[0] = 0   # El primero es cero pq ya estamos ahi

    for index in range(1, N):
        iterations = int(log2(index) + 1) # Este coso calcula cuantas potencias de 2 hay para index

        # Aca saltamos por cada potencia
        for k in range(iterations):
            i = index - 2 ** k

            if i >= 0:
                new_cost = DP[i] + abs(heights[i] - heights[index])
                DP[index] = min(DP[index], new_cost)    #Actualizo el costo mínimo para llegar al edificio actual

    return DP[N - 1]  # El costo mínimo queda guardado en DP[N-1]

N = int(sys.stdin.readline().rstrip())  # Primer input es la cantidad de edificios
heights = list(map(int, sys.stdin.readline().split()))  # Segundo input es la altura entre edificios empezando por el primero 

sys.stdout.write(f"{minimal_energy(N, heights)}\n")
